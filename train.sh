#!/bin/bash

# Preprocess data (optional step)
# python scripts/preprocess_data.py --input sample_data/train.csv --output sample_data/train_processed.csv

# Train the model
python scripts/train.py --config configs/train.yaml
