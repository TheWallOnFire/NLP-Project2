# 🤖 NLP in Industry - Project 2

Welcome to the **NLP-Project2** repository. This project contains a series of exercises and implementations developed for the *NLP in Industry* course. Each exercise focuses on practical applications of modern Natural Language Processing techniques, ranging from intent detection to advanced language model fine-tuning.

---

## 📂 Project Structure

The repository is organized into distinct exercises, each contained within its own directory:

| Directory | Topic | Status |
| :--- | :--- | :--- |
| [**Ex2/**](./Ex2) | **Banking Intent Detection** | ✅ Completed |
| [**Ex3/**](./Ex3) | **Future NLP Task** | 🚧 In Progress |

---

## 🛠️ Exercises Overview

### 🏦 [Ex2: Banking Intent Detection with Unsloth](./Ex2)
This exercise implements a high-performance intent detection system for the banking domain.
- **Key Features**: Fine-tuning Llama-3 8B using Unsloth (QLoRA), memory-efficient training, and generative classification.
- **Dataset**: BANKING77 (77 unique intents).
- **Tools**: Unsloth, HuggingFace, PyTorch.

### 🤖 [Ex3: Banking AI-Agent](./Ex3)
This exercise involves building an agentic workflow for banking customer support.
- **Key Features**: Multi-node pipeline (Intent, Priority, Policy, Draft, Validation, Router), Orchestration, and LLM integration.
- **Tools**: FastAPI, Ollama (gpt-oss-20b), Pydantic.
- **Integration**: Reuses the fine-tuned intent detection model from Ex2.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- CUDA-enabled GPU (Recommended for training)
- Virtual Environment (Recommended)

### General Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/TheWallOnFire/NLP-Project2.git
   cd NLP-Project2
   ```

2. Navigate to a specific exercise directory (e.g., `Ex2`) and follow the local `README.md` instructions for environment setup and execution.

---

## 🎓 About
Developed as part of the **NLP in Industry** course curriculum. This repository serves as a portfolio of advanced NLP implementations using state-of-the-art libraries and models.

---

## 🎥 Demonstration
A full video walkthrough of the training and inference process can be found here:
https://drive.google.com/file/d/1HjkPxZSVysf7W95rKNWbKijGxjcnpKxm/view?usp=sharing

---
*Developed for the NLP in Industry Course - Project 2.*
