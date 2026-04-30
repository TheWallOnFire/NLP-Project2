# 📋 Project 2 Summary: Fine-Tuning Intent Detection Model

This document provides a concise summary of the requirements, architecture, and objectives for **Project 2: Fine-Tuning Intent Detection Model with Banking Dataset**, based on the course documentation.

---

## 🎯 Project Objective
The primary goal is to study and apply fine-tuning techniques to a banking intent classification task. Students are required to:
- Sample and preprocess the **BANKING77** dataset.
- Fine-tune a Large Language Model (LLM) for generative classification.
- Evaluate the model's performance on a test set.
- Implement a standalone inference system.

---

## 🛠️ Technical Specifications
- **Model Framework**: [Unsloth](https://github.com/unslothai/unsloth) for fast and memory-efficient training.
- **Base Model**: Llama-3 8B (quantized to 4-bit).
- **Fine-Tuning Method**: QLoRA (Quantized Low-Rank Adaptation).
- **Dataset**: PolyAI BANKING77 (containing 77 unique banking intents).
- **Inference**: A Python class that loads the saved LoRA adapters and performs classification on input messages.

---

## 📂 Deliverables
1.  **Source Code**:
    - `scripts/preprocess_data.py`: Data cleaning and formatting.
    - `scripts/train.py`: Fine-tuning logic using Unsloth.
    - `scripts/inference.py`: Standalone inference class.
2.  **Configurations**: YAML files for training hyperparameters and inference settings.
3.  **Documentation**:
    - Hyperparameters (Batch size, Learning rate, Optimizer, Epochs).
    - Environment details (Google Colab, Kaggle, or Local).
4.  **Demonstration**: A video walkthrough showing the training process, inference execution, and final accuracy results.

---
*Summary generated for the NLP in Industry Course - Project 2.*
