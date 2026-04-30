from ..core.schemas import ValidationResult

class ValidationNode:
    def process(self, draft: str, policy: str) -> ValidationResult:
        # Simple validation logic: 
        # 1. Length check
        # 2. Basic hallucination check (does it mention something completely different?)
        
        if len(draft) < 10:
            return ValidationResult(is_valid=False, feedback="Response is too short.")
            
        # Basic check if it contains any mention of the policy keywords (dummy implementation)
        # In a real scenario, this might use another LLM call or NLI model
        
        return ValidationResult(is_valid=True)
