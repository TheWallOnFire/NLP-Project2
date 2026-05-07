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
