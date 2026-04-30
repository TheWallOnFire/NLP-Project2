from ..core.schemas import PolicyResult
from ..data.policies import BANKING_POLICIES

class PolicyNode:
    def process(self, intent: str) -> PolicyResult:
        # Retrieve policy based on intent
        policy = BANKING_POLICIES.get(intent, BANKING_POLICIES["default"])
        
        return PolicyResult(
            policy_snippet=policy["snippet"],
            source=policy["source"]
        )
