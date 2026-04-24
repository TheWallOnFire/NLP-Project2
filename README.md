# 🏦 Banking Intent Detection with Unsloth

This project implements a high-performance intent detection model for the banking domain using the **BANKING77** dataset and **Unsloth**.

## 🚀 Quick Start

### For Windows Users
1. **Install dependencies**: `pip install -r requirements.txt`
2. **Train model**: Double-click `train.bat`
3. **Run inference**: Double-click `inference.bat` (or run `inference.bat "message"` in CMD)

### For Linux/macOS/WSL Users
1. **Install dependencies**: `pip install -r requirements.txt`
2. **Train model**: `bash train.sh`
3. **Run inference**: `bash inference.sh`

## 📋 Assignment Details

This project fulfills the requirements for the **NLP in Industry - Project 2**:
- **Dataset**: [BANKING77](https://huggingface.co/datasets/PolyAI/banking77) (77 unique intents).
- **Fine-tuning**: Used **Unsloth** with 4-bit quantization and LoRA (QLoRA) for efficient training.
- **Approach**: Generative Intent Classification (the model is trained to generate the name of the intent).

## 🛠️ Project Structure

```text
├── configs/
│   ├── train.yaml          # Hyperparameters for training
│   └── inference.yaml      # Settings for inference
├── scripts/
│   ├── preprocess_data.py  # Data sampling & label mapping
│   ├── train.py           # Unsloth fine-tuning script
│   └── inference.py        # IntentClassification class & CLI
├── sample_data/
│   ├── train.csv           # Sampled training data
│   └── test.csv            # Sampled test data
├── models/
│   └── intent_model/       # Saved model checkpoint
├── train.sh                # Automation script for training
├── inference.sh            # Automation script for inference
└── requirements.txt        # Project dependencies
```

## ⚙️ Hyperparameters

| Parameter | Value |
|-----------|-------|
| Base Model | `llama-3-8b-bnb-4bit` |
| Learning Rate | `2e-4` |
| Batch Size | `2` (per device) |
| Gradient Acc. | `4` |
| Max Steps | `60` |
| Max Seq Length | `2048` |
| Optimizer | `adamw_8bit` |

## 🧪 Inference Implementation

The core logic is housed in the `IntentClassification` class found in `scripts/inference.py`. It provides a clean interface for predicting intents from text queries.

```python
from scripts.inference import IntentClassification

# Initialize classifier
classifier = IntentClassification("configs/inference.yaml")

# Predict intent
intent = classifier("I can't access my account.")
print(f"Predicted Intent: {intent}")
```

## 🎥 Video Demonstration
[View the Demonstration Video](YOUR_VIDEO_LINK_HERE)

---
*Developed for the Applications of Natural Language Processing in Industry course.*
