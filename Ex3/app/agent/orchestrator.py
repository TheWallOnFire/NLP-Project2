from ..core.schemas import QueryRequest, QueryResponse, AgentTrace, RoutingDecision
from ..clients.ollama_client import OllamaClient
from ..nodes.intent_node import IntentNode
from ..nodes.priority_node import PriorityNode
from ..nodes.policy_node import PolicyNode
from ..nodes.draft_node import DraftNode
from ..nodes.validation_node import ValidationNode
from ..nodes.router_node import RouterNode

class AgentOrchestrator:
    def __init__(self):
        self.ollama_client = OllamaClient()
        self.intent_node = IntentNode()
        self.priority_node = PriorityNode()
        self.policy_node = PolicyNode()
        self.draft_node = DraftNode(self.ollama_client)
        self.validation_node = ValidationNode()
        self.router_node = RouterNode()

    def run(self, request: QueryRequest) -> QueryResponse:
        print(f"\n--- [AGENT START] Processing: '{request.query}' ---")
        trace = AgentTrace()
        
        # 1. Intent Detection
        trace.intent = self.intent_node.process(request.query)
        print(f"DEBUG: [IntentNode] Identified: '{trace.intent.intent}' (Confidence: {trace.intent.confidence:.2f})")
        
        # 2. Priority Assessment
        trace.priority = self.priority_node.process(request.query)
        print(f"DEBUG: [PriorityNode] Level: {trace.priority.level}")
        
        # 3. Policy Retrieval
        trace.policy = self.policy_node.process(trace.intent.intent)
        print(f"DEBUG: [PolicyNode] Snippet: '{trace.policy.policy_snippet[:50]}...'")
        
        # 4. Response Drafting
        trace.draft = self.draft_node.process(
            query=request.query,
            intent=trace.intent.intent,
            priority=trace.priority.level,
            policy=trace.policy.policy_snippet
        )
        print(f"DEBUG: [DraftNode] Drafted Response (Len: {len(trace.draft.draft_response)})")
        
        # 5. Validation
        trace.validation = self.validation_node.process(
            trace.draft.draft_response,
            trace.draft.missing_information,
            trace.intent.confidence
        )
        print(f"DEBUG: [ValidationNode] Passed: {trace.validation.is_valid} (Reason: {trace.validation.feedback})")
        
        # 6. Routing Decision
        trace.router = self.router_node.process(
            trace.priority.level,
            trace.validation
        )
        print(f"DEBUG: [RouterNode] Decision: {trace.router.decision}")
        
        # Determine final response text based on routing
        final_response = trace.draft.draft_response
        if trace.router.decision == RoutingDecision.ESCALATE:
            final_response = f"I've drafted a response, but since this is a high-priority issue, I'm connecting you with a human specialist. {final_response}"
        elif trace.router.decision == RoutingDecision.ASK_MORE:
            final_response = "I'm not sure I fully understand. Could you please provide more details about your request?"

        print(f"--- [AGENT COMPLETE] Final Decision: {trace.router.decision} ---\n")

        return QueryResponse(
            query=request.query,
            response=final_response,
            trace=trace
        )
