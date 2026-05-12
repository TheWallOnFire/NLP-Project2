# 🏦 Banking AI-Agentic Workflow

An intelligent, node-based agentic workflow for banking customer support. This system leverages fine-tuned Large Language Models (LLMs) to understand customer intent, assess risk, and generate policy-grounded responses automatically.

## 🤖 Workflow Architecture

The system is built using a modular **"Chain of Thought"** architecture, where each node has a specialized responsibility:

1.  **Intent Detection**: Identifies the customer's goal using a **fine-tuned Llama-3 8B model** with an automatic **Keyword Fallback** for robustness.
2.  **Priority Assessment**: Evaluates the urgency and risk level (Low, Medium, High).
3.  **Policy Retrieval**: Fetches relevant banking guidelines from a curated policy database.
4.  **Response Drafting**: Generates a professional, empathetic response using **Ollama** (`llama3:8b` or `gpt-oss-20b`).
5.  **Validation**: Performs quality checks on the draft (completeness, accuracy, and confidence).
6.  **Routing/Escalation**: Determines if the response can be sent directly or if the case requires a human specialist.

---

## ✨ Key Features & Stability

- **Smart Model Detection**: The system automatically searches for model weights in `Ex3/models/`, `../Ex2/models/`, or the current working directory.
- **Robust Fallback**: If LLM weights are missing or a GPU is unavailable, the agent gracefully falls back to a rule-based keyword matcher, ensuring the service remains active.
- **Development Stability**: Optimized for `uvicorn` reloader—the server won't crash or loop due to model cache updates.
- **Colab Optimized**: Includes a robust tunneling setup for stable public access to both the API and the Web UI.

---

## 🚀 How to Run

### ☁️ Option 1: Google Colab (Highly Recommended)
Run the entire system—including the heavy LLaMA-3 training and Ollama LLM—for free on Google Colab using a T4 GPU.

1.  Open `Ex3/Run_App_Colab.ipynb` in Google Colab (T4 GPU).
2.  Follow the interactive prompts to either train the model natively or upload a pre-trained `intent_model.zip`.
3.  **Access the UI**: In Step 5, look for the `FRONTEND UI` link (ending in `.trycloudflare.com`). **Do not use the standard "External URL"** provided by Streamlit as it will timeout.

### 💻 Option 2: Local Execution
1.  **Prerequisites**: Python 3.10+, **Ollama** installed (`ollama pull llama3:8b`).
2.  **Setup**:
    ```bash
    # Create virtual environment
    python -m venv venv

    # Activate (Windows)
    .\venv\Scripts\activate

    # Activate (Linux/Mac)
    source venv/bin/activate

    # Install core dependencies
    pip install -r requirements.txt

    # (Optional) For AI Model support, install torch and unsloth
    pip install torch unsloth
    ```
3.  **Run**:
    ```bash
    python run.py
    ```
    *The agent will automatically check for the intent model in `models/intent_model/`. If not found, it will log an info message and use Keyword Fallback.*

---

## 📁 Project Structure
- `app/main.py`: FastAPI entry point and pipeline orchestration.
- `app/nodes/`: Specialized logic for each agent node (Intent, Priority, Policy, etc.).
- `app/core/`: Settings, schemas, and local LLM wrappers.
- `app/data/`: Internal policy database and bank guidelines.
- `frontend/`: Premium Streamlit web interface with deep reasoning trace.
- `models/`: (Ignored by Git) Directory for fine-tuned LLM weights.

## 🎓 Course Information
- **Course**: NLP in Industry (Project 3)
- **Instructor**: Dr. Nguyen Hong Buu Long
- **Institution**: University of Science - VNUHCM
- **Student**: Huynh Manh Tuong - 23120105
- **URL**: https://drive.google.com/file/d/1pbjYF9cHXyMEx2Qr8AI7Eo3qgnNVq2Co/view?usp=sharing
