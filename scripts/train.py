import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="Train the NLP model")
    parser.add_argument("--config", type=str, default="configs/train.yaml", help="Path to training config")
    args = parser.parse_args()
    
    print(f"Starting training with config: {args.config}")
    # Training logic here
    print("Training completed.")

if __name__ == "__main__":
    main()
