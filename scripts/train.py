import os
import torch
import yaml
import argparse
from unsloth import FastLanguageModel
from trl import SFTTrainer
from transformers import TrainingArguments
from datasets import load_dataset

def train():
    parser = argparse.ArgumentParser(description="Train the Intent Detection model with Unsloth")
    parser.add_argument("--config", type=str, default="configs/train.yaml", help="Path to training config")
    args = parser.parse_args()
    
    if not os.path.exists(args.config):
        print(f"Error: Config file {args.config} not found.")
        return

    with open(args.config, "r") as f:
        config = yaml.safe_load(f)

    print(f"Loading model: {config['model_name']}...")
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name = config["model_name"],
        max_seq_length = config.get("max_seq_length", 2048),
        load_in_4bit = config.get("load_in_4bit", True),
    )

    print("Setting up PEFT (LoRA)...")
    model = FastLanguageModel.get_peft_model(
        model,
        r = 16, # LoRA rank
        target_modules = ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
        lora_alpha = 16,
        lora_dropout = 0,
        bias = "none",
        use_gradient_checkpointing = "unsloth",
    )

    print(f"Loading training data from {config['train_data_path']}...")
    # Load dataset from CSV
    dataset = load_dataset("csv", data_files={"train": config["train_data_path"]})["train"]
    
    # Format prompts for SFT
    def formatting_prompts_func(examples):
        texts = []
        for text, intent in zip(examples["text"], examples["intent"]):
            # Prompt format consistent with inference, adding EOS token for training
            prompt = f"Instruction: Detect the banking intent of the following query.\nInput: {text}\nResponse: {intent}{tokenizer.eos_token}"
            texts.append(prompt)
        return { "text" : texts, }

    dataset = dataset.map(formatting_prompts_func, batched = True)

    print("Starting training...")
    
    # Version-agnostic trainer initialization
    print("Starting training...")
    
    trainer_args = dict(
        model = model,
        train_dataset = dataset,
        dataset_text_field = "text",
        max_seq_length = config.get("max_seq_length", 2048),
        dataset_num_proc = 2,
        packing = False,
        args = TrainingArguments(
            per_device_train_batch_size = config.get("batch_size", 2),
            gradient_accumulation_steps = 4,
            warmup_steps = 5,
            max_steps = config.get("max_steps", 60),
            learning_rate = float(config.get("learning_rate", 2e-4)),
            fp16 = not torch.cuda.is_bf16_supported(),
            bf16 = torch.cuda.is_bf16_supported(),
            logging_steps = 1,
            optim = config.get("optimizer", "adamw_8bit"),
            weight_decay = 0.01,
            lr_scheduler_type = "linear",
            seed = 3407,
            output_dir = "outputs",
            save_strategy = "no",
        ),
    )

    try:
        # Try the modern 'processing_class' argument first (trl >= 0.11.0)
        trainer = SFTTrainer(**trainer_args, processing_class = tokenizer)
    except TypeError:
        try:
            # Fallback to the legacy 'tokenizer' argument (trl < 0.11.0)
            trainer = SFTTrainer(**trainer_args, tokenizer = tokenizer)
        except TypeError as e:
            # Final fallback: If transformers >= 4.47 is causing issues, try passing processing_class via args
            print(f"Warning: Standard initialization failed ({e}). Attempting fallback...")
            trainer = SFTTrainer(**trainer_args)
            trainer.tokenizer = tokenizer # Manually attach it

    trainer_stats = trainer.train()
    print(f"Training completed! Stats: {trainer_stats}")

    print(f"Saving model and tokenizer to {config['output_dir']}...")
    os.makedirs(config["output_dir"], exist_ok=True)
    model.save_pretrained(config["output_dir"])
    tokenizer.save_pretrained(config["output_dir"])
    print("Model saved successfully.")

if __name__ == "__main__":
    train()
