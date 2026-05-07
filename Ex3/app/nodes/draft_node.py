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
4. If you don't have enough information, list the missing details.
5. Suggest the next logical action for the customer or the bank.

Format your response as follows:
RESPONSE: [Your draft response]
MISSING_INFO: [Detail 1, Detail 2, or None]
NEXT_ACTION: [Suggested action]
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
