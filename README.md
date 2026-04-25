# 🏦 Banking Intent Detection with Unsloth

[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TheWallOnFire/NLP-Project2/blob/main/Banking_Intent_Detection_Colab.ipynb)

This project implements a high-performance intent detection system for the banking domain. By leveraging **Unsloth** and **Llama-3 (8B)**, we achieve fast, memory-efficient fine-tuning (QLoRA) on the **BANKING77** dataset.

The model is trained to act as a generative classifier, identifying 77 unique banking-related intents from customer queries.

---

## 🚀 Quick Start Guide

### 💻 Running on local PC (Windows/Linux)

#### 1. Environment Setup
We recommend using a Python virtual environment:
```powershell
# Windows
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

# Linux/macOS/WSL
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### 2. Training the Model
Use the provided automation scripts to preprocess data, start training, and automatically calculate final accuracy:
- **Execution**: `bash train.sh`

#### 3. Running Inference
Once the model is saved in `models/intent_model/`, you can test it:
- **Execution**: `bash inference.sh "I lost my credit card, what should I do?"`

---

### ☁️ Running on Google Colab (Recommended)

Google Colab is the easiest way to run this project as it provides free access to T4 GPUs optimized for Unsloth.

1.  Open [Google Colab](https://colab.research.google.com).
2.  Upload the `Banking_Intent_Detection_Colab.ipynb` file from this repository.
3.  Set your Runtime to **GPU** (`Runtime > Change runtime type > T4 GPU`).
4.  Run the cells sequentially. The notebook will automatically clone the repository and handle all installations.

---

## 🛠️ Project Structure

```text
├── configs/
│   ├── train.yaml          # Hyperparameters (LR, Batch Size, Steps)
│   └── inference.yaml      # Model path and generation settings
├── scripts/
│   ├── preprocess_data.py  # Dataset sampling & prompt formatting
│   ├── train.py            # Unsloth fine-tuning & evaluation
│   └── inference.py        # IntentClassification class for predictions
├── sample_data/            # Local directory for processed CSVs
├── models/
│   └── intent_model/       # Destination for the fine-tuned LoRA weights
├── train.sh                # Automated Training & Evaluation
└── inference.sh            # Automated Inference script
```

---

## 📊 Model & Training Details

| Feature | Specification |
| :--- | :--- |
| **Base Model** | Meta Llama-3 8B (4-bit quantized) |
| **Dataset** | PolyAI BANKING77 (77 Intents) |
| **Fine-tuning** | QLoRA (Rank 16, Alpha 16) |
| **Optimization** | AdamW 8-bit (Unsloth optimized) |
| **Max Seq Length** | 2048 tokens |

---

## 🎥 Demonstration
A full video walkthrough of the training and inference process can be found here:
[**[Link to Video Demo]**](YOUR_VIDEO_LINK_HERE)

---
*Developed for the NLP in Industry Course - Project 2.*
