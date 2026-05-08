from ..clients.ollama_client import OllamaClient
from ..core.schemas import DraftResult, Priority

class DraftNode:
    def __init__(self, llm_client: OllamaClient):
        self.llm_client = llm_client

    def process(self, query: str, intent: str, priority: Priority, policy: str) -> DraftResult:
        prompt = f"""
You are an expert Banking Customer Support Assistant.
Customer Inquiry: "{query}"
Detected Intent: {intent}
Priority Level: {priority}
Relevant Bank Policy: "{policy}"

Task: Draft a professional and empathetic response to the customer.
Guidelines:
1. Address the customer's specific concern directly.
2. Incorporate the "Relevant Bank Policy" naturally into your answer.
3. If the priority is HIGH, lead with a reassuring statement about immediate action.
4. Keep the tone professional yet approachable.
5. If you need more information to process the request (e.g., date, transaction ID), explicitly list it.
6. Suggest the very next step the customer should take.

Format your output exactly as:
RESPONSE: [Your detailed draft]
MISSING_INFO: [What we still need, or 'None']
NEXT_ACTION: [What the user should do next]
"""
        
        try:
            raw_response = self.llm_client.generate(prompt, max_tokens=512)
            
            # Parse the structured response
            draft_response = "I'm sorry, I'm having trouble generating a response right now."
            missing_info = []
            next_action = "Please contact support for further assistance."
            
            for line in raw_response.split('\n'):
                if line.startswith("RESPONSE:"):
                    draft_response = line.replace("RESPONSE:", "").strip()
                elif line.startswith("MISSING_INFO:"):
                    info_str = line.replace("MISSING_INFO:", "").strip()
                    if info_str.lower() != "none" and info_str:
                        missing_info = [i.strip() for i in info_str.split(',')]
                elif line.startswith("NEXT_ACTION:"):
                    next_action = line.replace("NEXT_ACTION:", "").strip()
            
            return DraftResult(
                draft_response=draft_response,
                missing_information=missing_info,
                next_action=next_action
            )
        except Exception as e:
            print(f"Error drafting response: {e}")
            return DraftResult(
                draft_response="I'm sorry, I'm having trouble generating a response right now.",
                missing_information=[],
                next_action="Please try again later."
            )
