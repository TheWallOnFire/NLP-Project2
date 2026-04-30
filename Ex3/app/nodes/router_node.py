from ..core.schemas import RouterResult, RoutingDecision, Priority, ValidationResult

class RouterNode:
    def process(self, priority: Priority, validation: ValidationResult) -> RouterResult:
        # High priority items might need human review anyway
        if priority == Priority.HIGH:
            return RouterResult(
                decision=RoutingDecision.ESCALATE,
                explanation="High priority security issue. Escalating to human agent for safety."
            )
            
        # If validation failed
        if not validation.is_valid:
            return RouterResult(
                decision=RoutingDecision.ASK_MORE,
                explanation=f"Validation failed: {validation.feedback}. Asking customer for clarification."
            )
            
        return RouterResult(
            decision=RoutingDecision.SEND,
            explanation="Response is valid and priority is manageable. Sending to customer."
        )
