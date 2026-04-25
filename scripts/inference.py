import os
import torch
import yaml
import argparse
from unsloth import FastLanguageModel

class IntentClassification:
    """
    Standalone inference class for Banking Intent Detection.
    """
    def __init__(self, model_path):
        """
        Initialize the inference class by loading the configuration and model.
        Args:
            model_path (str): Path to the inference YAML configuration file.
        """
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Config file not found: {model_path}")

        with open(model_path, "r") as f:
            self.config = yaml.safe_load(f)

        if not torch.cuda.is_available():
            raise RuntimeError("CUDA is not available. Unsloth requires an NVIDIA GPU.")

        model_dir = self.config["model_path"]
        print(f"Loading model and tokenizer from {model_dir}...")
        
        # Load model and tokenizer
        self.model, self.tokenizer = FastLanguageModel.from_pretrained(
            model_name = model_dir,
            max_seq_length = self.config.get("max_seq_length", 2048),
            load_in_4bit = self.config.get("load_in_4bit", True),
        )
        
        # Switch to inference mode
        FastLanguageModel.for_inference(self.model)

    def __call__(self, message):
        """
        Predict the intent label for a given input message.
        Args:
            message (str): The customer query.
        Returns:
            str: The predicted intent label.
        """
        # Format the prompt consistent with training
        prompt = f"Instruction: Detect the banking intent of the following query.\nInput: {message}\nResponse: "
        
        inputs = self.tokenizer([prompt], return_tensors="pt").to("cuda")
        
        # Generate output
        outputs = self.model.generate(
            **inputs, 
            max_new_tokens = 64,
            use_cache = True,
            pad_token_id = self.tokenizer.eos_token_id
        )
        
        # Decode results
        result = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
        
        # Extract the label after the "Response:" part
        if "Response:" in result:
            # Take only the part after the LAST "Response:" and then only the first non-empty line
            predicted_label = result.split("Response:")[-1].strip().split('\n')[0].strip()
        else:
            predicted_label = result.strip().split('\n')[0].strip()
            
        return predicted_label

def main():
    parser = argparse.ArgumentParser(description="Run inference using the fine-tuned model")
    parser.add_argument("--config", type=str, default="configs/inference.yaml", help="Path to inference config")
    parser.add_argument("--message", type=str, help="Input message to classify")
    args = parser.parse_args()

    # Create the classifier
    try:
        classifier = IntentClassification(args.config)
    except Exception as e:
        print(f"Error initializing classifier: {e}")
        return

    # Use the classifier
    if args.message:
        label = classifier(args.message)
        print(f"\nInput: {args.message}")
        print(f"Predicted Intent: {label}")
    else:
        # Example usage as requested in the PDF
        test_messages = [
            "I want to check my account balance.",
            "I lost my credit card, what should I do?",
            "The ATM swallowed my card."
        ]
        print("\n--- Running examples ---")
        for msg in test_messages:
            label = classifier(msg)
            print(f"- Input: {msg}")
            print(f"  Result: {label}\n")

if __name__ == "__main__":
    main()
