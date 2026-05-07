import os
import sys
from ..core.schemas import IntentResult
from ..core.settings import settings

# Attempt to import the Lab 2 inference class
try:
    # The project root was added to sys.path in run.py
    from Ex2.scripts.inference import IntentClassification
    HAS_LAB2_MODEL = True
except ImportError:
    HAS_LAB2_MODEL = False

class IntentNode:
    """
    Intent classification for banking customer support.
    Uses the fine-tuned model from Lab 2 as the primary classifier,
    with a rule-based fallback for robustness.
    """
    
    def __init__(self):
        self.classifier = None
        self.use_fallback = not HAS_LAB2_MODEL
        
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
        
        # Initialize Lab 2 classifier if available
        if HAS_LAB2_MODEL:
            config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", settings.INTENT_CONFIG_PATH))
            if os.path.exists(config_path):
                try:
                    # Note: This requires a GPU and the models folder to exist
                    self.classifier = IntentClassification(config_path)
                    print(f"✅ Lab 2 Intent Model loaded from {config_path}")
                except Exception as e:
                    print(f"⚠️ Failed to initialize Lab 2 model: {e}. Falling back to rules.")
                    self.use_fallback = True
            else:
                print(f"⚠️ Lab 2 config not found at {config_path}. Falling back to rules.")
                self.use_fallback = True

    def process(self, message: str) -> IntentResult:
        """
        Process a customer message and return the detected intent.
        """
        message_lower = message.lower().strip()
        
        # 1. Try using the fine-tuned model first
        if not self.use_fallback and self.classifier:
            try:
                intent = self.classifier(message)
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
