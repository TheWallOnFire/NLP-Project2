from ..core.schemas import ValidationResult

class ValidationNode:
    def process(self, draft: str, missing_info: list, intent_confidence: float) -> ValidationResult:
        """
        Validate the generated response.
        """
        # 1. Check for missing information reported by the draft node
        if missing_info:
            return ValidationResult(
                is_valid=False,
                feedback=f"Missing critical information: {', '.join(missing_info)}"
            )
            
        # 2. Check for minimum response length
        if len(draft) < 20:
            return ValidationResult(is_valid=False, feedback="Response is too brief and may be incomplete.")
            
        # 3. Check for intent confidence
        if intent_confidence < 0.6:
            return ValidationResult(is_valid=False, feedback="Low intent detection confidence. Need clarification.")
            
        return ValidationResult(is_valid=True)
