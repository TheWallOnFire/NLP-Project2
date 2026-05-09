import os
import sys
from ..core.schemas import IntentResult
from ..core.settings import settings

try:
    from .intent_classifier_wrapper import LocalIntentClassifier
    HAS_INTENT_MODEL_CODE = True
except Exception as e:
    print(f"⚠️ Could not load Intent Classifier (GPU might be missing): {e}")
    HAS_INTENT_MODEL_CODE = False

class IntentNode:
    """
    Intent classification for banking customer support.
    Uses the fine-tuned model from Lab 2 as the primary classifier,
    with a rule-based fallback for robustness.
    """
    
    def __init__(self):
        self.classifier = None
        self.use_fallback = not HAS_INTENT_MODEL_CODE
        
        # Define keyword patterns for fallback logic
        self.intent_patterns = {
            "card_lost": ["lost", "stolen", "missing", "can't find", "misplaced"],
            "balance_inquiry": ["balance", "how much", "account balance", "check balance"],
            "transfer_failure": ["transfer", "failed", "fail", "error", "declined"],
            "blocked_account": ["blocked", "lock", "frozen", "pin", "disabled"],
            "refund_request": ["refund", "chargeback", "return", "dispute"],
            "loan_inquiry": ["loan", "mortgage", "credit", "interest rate"],
            "transaction_history": ["transaction", "history", "statement", "recent"]
        }
        
        # Initialize Local classifier if available
        if HAS_INTENT_MODEL_CODE:
            # We look for the config file path defined in settings
            config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", settings.INTENT_CONFIG_PATH))
            
            if os.path.exists(config_path):
                try:
                    # Note: This requires a GPU and the models folder to exist
                    self.classifier = LocalIntentClassifier(config_path)
                    print(f"✅ Local Intent Model loaded from {config_path}")
                except Exception as e:
                    print(f"⚠️ Failed to initialize local model: {e}. Falling back to rules.")
                    self.use_fallback = True
            else:
                # If the project is standalone, try looking for the config in the core folder
                local_config = os.path.join(os.path.dirname(__file__), "../core/inference.yaml")
                if os.path.exists(local_config):
                    try:
                        self.classifier = LocalIntentClassifier(local_config)
                        print(f"✅ Local Intent Model loaded from {local_config}")
                    except Exception as e:
                        print(f"⚠️ Failed to initialize local model: {e}")
                        self.use_fallback = True
                else:
                    print(f"⚠️ Intent config not found at {config_path}. Falling back to rules.")
                    self.use_fallback = True

    def process(self, message: str) -> IntentResult:
        """
        Process a customer message and return the detected intent.
        """
        message_lower = message.lower().strip()
        
        # 1. Try using the fine-tuned model first
        if not self.use_fallback and self.classifier:
            try:
                intent = self.classifier.predict(message)
                # Map model output to our known intents if necessary
                # The Lab 2 model typically returns the intent name directly
                return IntentResult(intent=intent, confidence=0.90)
            except Exception as e:
                print(f"Error during model inference: {e}")
        
        # 2. Fallback to rule-based matching
        for intent, keywords in self.intent_patterns.items():
            if any(keyword in message_lower for keyword in keywords):
                return IntentResult(intent=intent, confidence=0.75)
        
        return IntentResult(intent="general", confidence=0.5)
