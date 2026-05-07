# 🏦 Banking AI-Agentic Workflow

This project implements an agentic workflow for banking customer support. It uses a series of specialized nodes to process customer queries, assess risk, retrieve policies, and generate professional responses.

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

### 1. Prerequisites
- Python 3.10+
- **Ollama** installed and running.
- **gpt-oss-20b** model pulled (`ollama pull gpt-oss:20b`).
- **Lab 2 Model**: Ensure your fine-tuned model is saved in `Ex2/models/intent_model/`.

### 2. Environment Setup
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Or .\venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration
Copy the sample config or set environment variables:
- `OLLAMA_BASE_URL`: Your Ollama server address (default: `http://localhost:11434`).
- `INTENT_CONFIG_PATH`: Path to the Ex2 inference configuration.

### 4. Running the Agent
```bash
python run.py
```
The API will be available at `http://localhost:8000`. You can access the interactive documentation at `http://localhost:8000/docs`.

### ☁️ Running with Google Colab (Free GPU)
If you don't have a strong enough machine to run Ollama locally, you can host the model on Google Colab and connect to it from your local FastAPI app.

1. Open the `docs/notebooks/Ollama-Pinggy.ipynb` notebook in Google Colab.
2. Change the Runtime type to **T4 GPU**.
3. Run the first cell to install and start Ollama in the background.
4. Run the second cell to pull the `gpt-oss:20b` model.
5. Open a terminal in Colab (or create a new cell) and run the Pinggy command to create a public tunnel to your Ollama instance:
   ```bash
   ssh -p 443 -R0:localhost:11434 qr@a.pinggy.io
   ```
6. Copy the public URL provided by Pinggy.
7. On your local machine, update your `configs/default.yaml` or environment variables to set `OLLAMA_BASE_URL` to the Pinggy URL.
8. Run `python run.py` locally!

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
