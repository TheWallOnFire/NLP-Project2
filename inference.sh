#!/bin/bash

# Run inference with the fine-tuned model
# You can pass a message argument: ./inference.sh "Hello, my card is stolen"
if [ -z "$1" ]; then
    python scripts/inference.py --config configs/inference.yaml
else
    python scripts/inference.py --config configs/inference.yaml --message "$1"
fi
