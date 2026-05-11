import os
import torch
import yaml
from unsloth import FastLanguageModel

class LocalIntentClassifier:
    """
    Local inference class for Banking Intent Detection, migrated from Project 2.
    """
    def __init__(self, config_path):
        """
        Initialize the inference class by loading the configuration and model.
        Args:
            config_path (str): Path to the inference YAML configuration file.
        """
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found: {config_path}")

        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)

        if not torch.cuda.is_available():
            raise RuntimeError("CUDA is not available. Unsloth requires an NVIDIA GPU.")

        model_dir = self.config["model_path"]
        
        # Adjust path if it's relative to the config file or absolute
        if not os.path.isabs(model_dir):
             # Try relative to the config file location
             potential_path = os.path.join(os.path.dirname(config_path), model_dir)
             if os.path.exists(potential_path):
                 model_dir = potential_path
             else:
                 # Fallback: check Ex2 folder directly if running locally
                 # Config is at app/core/inference.yaml. ../../../Ex2/models/intent_model gets us to NLP-Project2/Ex2/models/intent_model
                 ex2_path = os.path.join(os.path.dirname(config_path), "..", "..", "..", "Ex2", "models", "intent_model")
                 if os.path.exists(ex2_path):
                     model_dir = os.path.abspath(ex2_path)
                 else:
                     # Check if it was extracted directly to Ex3/models/intent_model
                     ex3_path = os.path.join(os.path.dirname(config_path), "..", "..", "models", "intent_model")
                     if os.path.exists(ex3_path):
                         model_dir = os.path.abspath(ex3_path)

        print(f"Loading Llama-3 Intent Model from {model_dir}...")
        
        # Load model and tokenizer
        self.model, self.tokenizer = FastLanguageModel.from_pretrained(
            model_name = model_dir,
            max_seq_length = self.config.get("max_seq_length", 2048),
            load_in_4bit = self.config.get("load_in_4bit", True),
        )
        
        # Switch to inference mode
        FastLanguageModel.for_inference(self.model)

    def predict(self, message):
        """
        Predict the intent label for a given input message.
        """
        # Format the prompt consistent with training
        prompt = f"Instruction: Detect the banking intent of the following query.\nInput: {message}\nResponse: "
        
        inputs = self.tokenizer([prompt], return_tensors="pt").to("cuda")
        
        # Generate output
        outputs = self.model.generate(
            **inputs, 
            max_new_tokens = 64,
            use_cache = True,
            pad_token_id = self.tokenizer.eos_token_id,
            max_length = None # Explicitly unset to avoid conflict with max_new_tokens
        )
        
        # Decode results
        result = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
        
        # Extract the label after the "Response:" part
        if "Response:" in result:
            predicted_label = result.split("Response:")[-1].strip().split('\n')[0].strip()
        else:
            predicted_label = result.strip().split('\n')[0].strip()
            
        return predicted_label
