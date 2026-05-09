# 🏦 Banking AI-Agentic Workflow

An intelligent, node-based agentic workflow for banking customer support. This system leverages fine-tuned Large Language Models (LLMs) to understand customer intent, assess risk, and generate policy-grounded responses automatically.

## 🤖 Workflow Architecture

The system is built using a modular **"Chain of Thought"** architecture, where each node has a specialized responsibility:

1.  **Intent Detection**: Identifies the customer's goal (e.g., balance inquiry, card lost) using a **fine-tuned Llama-3 8B model**.
2.  **Priority Assessment**: Evaluates the urgency and risk level (Low, Medium, High).
3.  **Policy Retrieval**: Fetches relevant banking guidelines from a curated policy database.
4.  **Response Drafting**: Generates a professional, empathetic response using **Ollama** (`gpt-oss-20b`).
5.  **Validation**: Performa quality checks on the draft (completeness, accuracy, and confidence).
6.  **Routing/Escalation**: Determines if the response can be sent directly or if the case requires a human specialist.

---

## 🚀 How to Run

Because this project relies heavily on the **fine-tuned LLaMA-3 intent model** from Ex2, you must obtain those trained model weights before the Ex3 Agent can function. We have designed interactive prompts in both local and Colab environments to make this easy!

### ☁️ Option 1: Google Colab (Highly Recommended)
Run the entire system—including the heavy LLaMA-3 training and Ollama LLM—for free on Google Colab using a T4 GPU.

**Step 1: Train the Model (Ex2)**
1. Open `Ex2/Banking_Intent_Detection_Colab.ipynb` in Google Colab (T4 GPU).
2. Run the cells. When prompted, type `clone` to pull the repository.
3. The final cell will train the intent model, automatically zip it (`intent_model.zip`), and download it to your physical computer.

**Step 2: Run the Banking Agent (Ex3)**
1. Open `Ex3/Run_App_Colab.ipynb` in Google Colab (T4 GPU).
2. When prompted for Git action, type `clone`.
3. When prompted: `Do you want to run Ex2 training inside this notebook? (y/n)`, type **`n`**.
4. The notebook will prompt you to **Upload** a file. Select the `intent_model.zip` you downloaded in Step 1.
5. The notebook will extract your model, boot up Ollama, and generate public Cloudflare URLs for your Streamlit Web UI!

---

### 💻 Option 2: Local Execution (Windows/Linux/Mac)
Perfect for development, but **requires an NVIDIA GPU** if you choose to run the training phase locally.

**1. Prerequisites**
- Python 3.10+
- **Ollama** installed ([ollama.com](https://ollama.com/))
- Download the Ollama model: `ollama pull gpt-oss:20b`
- **NVIDIA GPU** with CUDA installed (Only required if you are training the Ex2 model locally).

**2. Setup**
```bash
# Clone the repository
git clone https://github.com/TheWallOnFire/NLP-Project2.git
cd NLP-Project2/Ex3

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

**3. Run the Automated Script**
```powershell
# Windows PowerShell
powershell -ExecutionPolicy Bypass -File .\start_all.ps1
```
> **What this does:** The script will pause and ask: `Do you want to run the Ex2 training pipeline first? (y/n)`. 
> - If you type **`y`**: It will natively train the model via QLoRA (requires GPU), then boot up Ex3.
> - If you type **`n`**: It will skip training (assuming you already have the model in `Ex2/models/intent_model/`) and instantly start the FastAPI Backend and Streamlit Frontend!

---

## 📁 Project Structure
The project follows a professional modular structure as per requirements:
- `app/main.py`: FastAPI entry point.
- `app/nodes/`: Specialized logic for each agent node.
- `app/core/`: Settings, schemas, and model configurations.
- `app/data/`: Internal policy database.
- `frontend/`: Premium Streamlit web interface with voice support.
- `examples/`: Sample JSON requests for testing.

## 🎓 Course Information
- **Course**: NLP in Industry (Project 3)
- **Instructor**: Dr. Nguyen Hong Buu Long
- **Institution**: University of Science - VNUHCM
