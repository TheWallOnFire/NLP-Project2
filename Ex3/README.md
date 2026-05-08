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

### 💻 Option 1: Local Execution (Windows/Linux/Mac)
Perfect for development and high-performance hardware.

**1. Prerequisites**
- Python 3.10+
- **Ollama** installed ([ollama.com](https://ollama.com/))
- Download the model: `ollama pull gpt-oss:20b`

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

**3. Run**
- **Automatic**: Run `.\start_all.ps1` (PowerShell) to launch everything.
- **Manual**:
    - Terminal 1: `python run.py` (FastAPI Backend)
    - Terminal 2: `streamlit run frontend/app.py` (Web UI)

---

### ☁️ Option 2: Google Colab (Recommended for GPU)
Run the entire system—including the heavy LLM—for free on Google Colab.

1.  Upload the **`Run_App_Colab.ipynb`** file to your Google Colab.
2.  Change the Runtime type to **T4 GPU** (Runtime > Change runtime type).
3.  Run the cells sequentially.
4.  **Access the App**: The notebook uses **Cloudflare Tunnels** to provide stable public URLs for both the API and the Streamlit Web Interface. No local setup is required!

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
