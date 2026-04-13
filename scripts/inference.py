import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="Run inference with the NLP model")
    parser.add_argument("--config", type=str, default="configs/inference.yaml", help="Path to inference config")
    args = parser.parse_args()
    
    print(f"Running inference with config: {args.config}")
    # Inference logic here
    print("Inference completed.")

if __name__ == "__main__":
    main()
