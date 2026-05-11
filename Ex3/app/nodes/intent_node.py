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
        
        # 1. Check if model code is even available (unsloth installed)
        if not HAS_INTENT_MODEL_CODE:
            print("ℹ️ Unsloth not installed. Using Keyword Fallback for Intent Detection.")
            return

        # 2. Search for the model weights folder in common locations
        # We look for the folder in Ex3/models/intent_model or sibling Ex2
        possible_paths = [
            os.path.abspath(os.path.join(os.path.dirname(__file__), "../../models/intent_model")),
            os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../Ex2/models/intent_model")),
            os.path.abspath(os.path.join(os.getcwd(), "models/intent_model")),
            os.path.abspath(os.path.join(os.getcwd(), "../Ex2/models/intent_model"))
        ]
        
        found_path = None
        for p in possible_paths:
            if os.path.exists(os.path.join(p, "config.json")):
                found_path = p
                break
        
        # 3. Attempt to load the model if weights were found
        if found_path:
            try:
                # Use the core inference config if it exists, otherwise use the found directory
                config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../core/inference.yaml"))
                if not os.path.exists(config_path):
                    config_path = found_path
                
                self.classifier = LocalIntentClassifier(config_path)
                print(f"✅ AI Intent Model loaded successfully from: {found_path}")
                self.use_fallback = False
            except Exception as e:
                print(f"⚠️ Found model weights but failed to initialize LLM: {e}")
                print("ℹ️ Falling back to Keyword Rules.")
                self.use_fallback = True
        else:
            print("⚠️ Intent model weights not found in Ex3/models/intent_model.")
            print("ℹ️ Using Keyword Fallback. (To use the AI model, please extract your weights to Ex3/models/intent_model)")
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
