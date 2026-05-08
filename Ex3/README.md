# 🏦 Banking AI-Agentic Workflow

This project implements an agentic workflow for banking customer support. It uses a series of specialized nodes to process customer queries, assess risk, retrieve policies, and generate professional responses.

The project includes both a **FastAPI backend** and a **Streamlit web frontend** with voice capabilities.

---

## 🤖 Workflow Architecture

The system follows a modular "Chain of Thought" or "Node-based" design:

1.  **Intent Detection**: Identifies the user's goal using the fine-tuned **Llama-3 8B** model from **Lab 2**.
2.  **Priority Assessment**: Analyzes the urgency and risk level (Low/Medium/High).
3.  **Policy Retrieval**: Fetches relevant information from the internal knowledge base (`policies.py`).
4.  **Response Drafting**: Generates a tailored response using **Ollama** (`gpt-oss-20b`), including missing info and next steps.
5.  **Validation**: Verifies the drafted response for quality, completeness, and confidence.
6.  **Routing**: Decides whether to send the response directly, ask for more info, or escalate to a human agent.

---

## 🚀 Getting Started

There are three ways to run this project depending on your hardware capabilities.

### 💻 Option 1: Fully Local (Requires strong hardware)
Run both the FastAPI application and the Ollama model on your local machine.

**1. Prerequisites**
- Python 3.10+
- **Ollama** installed and running locally.
- Pull the model: `ollama pull gpt-oss:20b`.
- **Model Weights**: Copy your `models/intent_model/` from Project 2 into the `Ex3/models/` directory.

**2. Setup & Run**
```bash
# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run the Application
python run.py
```

### ☁️ Option 2: Google Colab (Recommended)
Run the entire system directly on Google Colab using our automated notebook.

1. Open **`Run_App_Colab.ipynb`** in Google Colab.
2. Change the Runtime to **T4 GPU**.
3. Run all cells. 
4. **Cloudflare Tunnel**: The notebook now uses `cloudflared` for superior stability. It will provide you with a clean `.trycloudflare.com` URL for the Web Frontend.

---

## 🏗️ Standalone Architecture
The project has been updated to be fully standalone. The **Intent Detection** logic from Project 2 has been migrated into `app/utils/intent_classifier.py`.

- `app/utils/intent_classifier.py`: Contains the local inference logic for the Llama-3 model.
- `configs/inference.yaml`: Manages model parameters locally within Ex3.
- `models/`: Destination folder for your fine-tuned model weights.

---

## 🧪 Testing
You can test the endpoint using `curl` or the provided `examples/sample_requests.json`:

```bash
curl -X POST "http://localhost:8000/process" \
     -H "Content-Type: application/json" \
     -d '{"query": "I lost my credit card, help!"}'
```

---

## 🎓 Project Details
- **Course**: NLP in Industry
- **Project**: 3 - Build a Banking AI-Agent
- **Instructor**: Dr. Nguyen Hong Buu Long

---

## 🏗️ Project Structure & Documentation

The project has been refactored to follow professional Python standards.

- `app/`: Main application code (FastAPI, agent nodes, etc.)
- `configs/`: Configuration YAML files.
- `docs/`: Comprehensive documentation. See [setup.md](docs/setup.md), [api.md](docs/api.md), and [architecture.md](docs/architecture.md) for more details.
- `tests/`: Unit and integration tests.

### Running Tests

To run the test suite, use pytest:
```bash
pytest
```
