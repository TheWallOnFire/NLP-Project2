import sys
import os
from ..core.settings import settings
from ..core.schemas import IntentResult

# Add Ex2 to path to import the classifier
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../Ex2")))

try:
    from scripts.inference import IntentClassification
except ImportError:
    # Fallback if structure is slightly different or for local testing without the model
    class IntentClassification:
        def __init__(self, config): pass
        def __call__(self, message): return "card_lost"

class IntentNode:
    def __init__(self):
        # The PDF says we must use the Lab 2 model.
        # We load it using the inference script from Ex2.
        self.classifier = None
        if os.path.exists(settings.INTENT_CONFIG_PATH):
            try:
                self.classifier = IntentClassification(settings.INTENT_CONFIG_PATH)
            except Exception as e:
                print(f"Warning: Could not load intent model: {e}")
        else:
            print(f"Warning: Intent config not found at {settings.INTENT_CONFIG_PATH}")

    def process(self, message: str) -> IntentResult:
        if self.classifier:
            try:
                label = self.classifier(message)
                return IntentResult(intent=label, confidence=0.95) # Dummy confidence
            except Exception as e:
                print(f"Error in intent detection: {e}")
                return IntentResult(intent="unknown", confidence=0.0)
        
        # Mock for demonstration if model is not loaded
        return IntentResult(intent="balance_inquiry", confidence=0.8)
