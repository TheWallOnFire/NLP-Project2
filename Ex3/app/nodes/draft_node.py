from ..clients.ollama_client import OllamaClient
from ..core.schemas import DraftResult, Priority

class DraftNode:
    def __init__(self, llm_client: OllamaClient):
        self.llm_client = llm_client

    def process(self, query: str, intent: str, priority: Priority, policy: str) -> DraftResult:
        prompt = f"""
You are a helpful and professional banking assistant.
Customer Query: "{query}"
Detected Intent: {intent}
Priority Level: {priority}
Relevant Policy: "{policy}"

Instructions:
1. Draft a concise and friendly response to the customer.
2. If the priority is HIGH, emphasize that we are handling this with urgency.
3. Use the information in the Relevant Policy to answer the query accurately.
4. If you don't have enough information, ask the customer for specific details.

Response:"""
        
        try:
            response_text = self.llm_client.generate(prompt, max_tokens=256)
            return DraftResult(draft_response=response_text.strip())
        except Exception as e:
            print(f"Error drafting response: {e}")
            return DraftResult(draft_response="I'm sorry, I'm having trouble generating a response right now. Please try again later.")
