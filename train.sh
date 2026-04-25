#!/bin/bash

# Preprocess data first to ensure sample_data is ready
echo "Step 1: Preprocessing data..."
python scripts/preprocess_data.py --train_size 1000 --test_size 200

# Train the model using Unsloth
echo "Step 2: Training the model..."
python scripts/train.py --config configs/train.yaml

# Evaluate the model
echo "Step 3: Evaluating the model..."
python scripts/evaluate.py --config configs/inference.yaml --test_data sample_data/test.csv

echo "Pipeline completed successfully!"
