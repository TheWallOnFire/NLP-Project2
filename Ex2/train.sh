#!/bin/bash

# Preprocess data first to ensure sample_data is ready
echo "Step 1: Preprocessing data..."
python scripts/preprocess_data.py --train_size 1000 --test_size 200

# Train the model using Unsloth
echo "Step 2: Training the model..."
python scripts/train.py --config configs/train.yaml

echo "Pipeline completed successfully!"
