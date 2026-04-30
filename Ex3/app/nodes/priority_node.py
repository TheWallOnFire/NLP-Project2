from ..core.schemas import Priority, PriorityResult

class PriorityNode:
    def __init__(self):
        # Critical keywords for banking
        self.high_priority_keywords = ["lost", "stolen", "stuck", "fraud", "stolen", "emergency", "hacked", "blocked"]
        self.medium_priority_keywords = ["problem", "error", "failed", "cannot", "declined"]

    def process(self, message: str) -> PriorityResult:
        message_lower = message.lower()
        
        # Simple rule-based logic as requested
        if any(kw in message_lower for kw in self.high_priority_keywords):
            return PriorityResult(
                level=Priority.HIGH,
                reason="Detected critical keyword related to security or immediate loss."
            )
        
        if any(kw in message_lower for kw in self.medium_priority_keywords):
            return PriorityResult(
                level=Priority.MEDIUM,
                reason="Detected operational issue or transaction failure."
            )
            
        return PriorityResult(
            level=Priority.LOW,
            reason="Standard inquiry without critical urgency markers."
        )
