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
*(A step-by-step guide is also available in `docs/notebooks/Run_Project_Local.ipynb`)*

**1. Prerequisites**
- Python 3.10+
- **Ollama** installed and running locally.
- Pull the model: `ollama pull gpt-oss:20b`.
- **Lab 2 Model**: Ensure your fine-tuned model is saved in `Ex2/models/intent_model/`.

**2. Setup & Run**
```bash
# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate  # Windows (or source venv/bin/activate on Linux/Mac)

# Install dependencies
pip install -r requirements.txt

# Run the Backend
python run.py

# Run the Frontend (in a new terminal)
streamlit run frontend/app.py
```
The API will be available at `http://localhost:8000` and the web interface at `http://localhost:8501`.

### ☁️ Option 2: Fully Google Colab (Free GPU, No local setup)
Run the entire system—Ollama, the FastAPI Backend, and the **Streamlit Frontend**—directly on Google Colab.

*(An automated notebook for this setup is available as `Run_App_Colab.ipynb` in the root directory. Just open it in Colab and follow the instructions!)*

**Manual Steps:**
1. Open a new Google Colab notebook and change the Runtime to **T4 GPU**.
2. Clone this repository into the Colab environment and enter the directory:
   ```bash
   !git clone https://github.com/TheWallOnFire/NLP-Project2.git
   %cd NLP-Project2/Ex3
   ```
3. Install the project dependencies:
   ```bash
   !pip install -r requirements.txt
   ```
4. Install and start Ollama in the background, then pull the model:
   ```bash
   !apt-get update -qq && apt-get install -y zstd
   !curl -fsSL https://ollama.com/install.sh | sh
   !ollama serve &
   !sleep 5 && ollama pull gpt-oss:20b
   ```
5. Use `localtunnel` or `ngrok` to expose the FastAPI port, then run the app:
   ```bash
   !npm install -g localtunnel
   !python run.py &
   !lt --port 8000
   ```
   *Access your API using the public URL provided by localtunnel.*

### 🔗 Option 3: Hybrid (Colab for Ollama, Local for App)
Host the heavy LLM on Google Colab, but run the FastAPI application locally.

1. Open the `docs/notebooks/Ollama-Pinggy.ipynb` notebook in Google Colab.
2. Change the Runtime type to **T4 GPU**.
3. Run the notebook cells to install Ollama and pull `gpt-oss:20b`.
4. Run the Pinggy command in Colab to create a public tunnel for Ollama:
   ```bash
   ssh -p 443 -R0:localhost:11434 qr@a.pinggy.io
   ```
5. **Copy the public URL** provided by Pinggy.
6. On your local machine, setup your environment (as shown in Option 1) but update `configs/default.yaml` (or set the environment variable) to point `OLLAMA_BASE_URL` to your Pinggy URL.
7. Run the app locally:
   ```bash
   python run.py
   ```

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
