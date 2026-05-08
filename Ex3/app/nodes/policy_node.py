from ..core.schemas import PolicyResult
from ..data.policies import BANKING_POLICIES

class PolicyNode:
    def process(self, intent: str) -> PolicyResult:
        # Retrieve policy based on intent, fallback to 'general'
        policy = BANKING_POLICIES.get(intent, BANKING_POLICIES.get("general"))
        
        # Double safety check
        if not policy:
            policy = {
                "snippet": "Please contact our support for more information regarding this request.",
                "source": "General Support"
            }
        
        return PolicyResult(
            policy_snippet=policy["snippet"],
            source=policy["source"]
        )
