# 🔄 Project Refactoring Plan: Banking AI-Agent (Ex3)

## 📋 Executive Summary

This document outlines a comprehensive plan to refactor the Banking AI-Agent project structure for better organization, maintainability, and adherence to Python best practices.

---

## 🎯 Objectives

1. **Clean up root directory** - Remove clutter and organize files logically
2. **Improve project structure** - Follow Python packaging standards
3. **Enhance maintainability** - Clear separation of concerns
4. **Better documentation** - Organized docs and examples
5. **Professional layout** - Industry-standard project structure

---

## 📁 Current Structure Issues

### Root Directory Clutter
```
Ex3/
├── .env.example          ✓ Keep
├── .gitignore            ✓ Keep
├── Build a Banking AI-Agent.pdf  → Move to docs/
├── Ollama-Pinggy.ipynb   → Move to docs/notebooks/
├── README.md             ✓ Keep
├── requirements.txt      ✓ Keep (or migrate to pyproject.toml)
├── run.py                ✓ Keep
├── summary.md            → Move to docs/
├── app/                  ✓ Keep
├── configs/              ⚠ Empty, needs content
├── examples/             ✓ Keep
└── scripts/              ✓ Keep
```

### Missing Components
- ❌ No dedicated `docs/` directory
- ❌ No proper `tests/` structure
- ❌ No `pyproject.toml` (modern Python standard)
- ❌ Empty `configs/` directory
- ❌ No clear test organization

---

## 🏗️ Proposed Structure

```
Ex3/
├── 📄 Configuration & Metadata
│   ├── .env.example              # Environment template
│   ├── .gitignore                # Git ignore rules
│   ├── requirements.txt          # Python dependencies
│   ├── pyproject.toml            # Project metadata (NEW)
│   └── README.md                 # Main documentation
│
├── 🚀 Application Code
│   ├── run.py                    # Entry point
│   └── app/                      # Main application package
│       ├── __init__.py
│       ├── main.py               # FastAPI app
│       ├── agent/                # Orchestrator
│       │   ├── __init__.py
│       │   └── orchestrator.py
│       ├── clients/              # External clients
│       │   ├── __init__.py
│       │   ├── base.py
│       │   └── ollama_client.py
│       ├── core/                 # Core functionality
│       │   ├── __init__.py
│       │   ├── schemas.py        # Pydantic models
│       │   └── settings.py       # Configuration
│       ├── nodes/                # Workflow nodes
│       │   ├── __init__.py
│       │   ├── intent_node.py
│       │   ├── priority_node.py
│       │   ├── policy_node.py
│       │   ├── draft_node.py
│       │   ├── validation_node.py
│       │   └── router_node.py
│       └── data/                 # Static data
│           ├── __init__.py
│           └── policies.py       # Banking policies
│
├── ⚙️ Configuration Files
│   └── configs/                  # Application configs
│       ├── default.yaml          # Default settings (NEW)
│       └── inference.yaml        # Model inference config (if needed)
│
├── 📚 Documentation
│   └── docs/                     # Documentation (NEW)
│       ├── architecture.md       # System architecture (NEW)
│       ├── api.md               # API documentation (NEW)
│       ├── setup.md             # Setup guide (NEW)
│       ├── project_summary.md   # Moved from summary.md
│       ├── "Build a Banking AI-Agent.pdf"  # Moved from root
│       └── notebooks/
│           └── Ollama-Pinggy.ipynb  # Moved from root
│
├── 🧪 Testing
│   └── tests/                    # Test suite (NEW)
│       ├── __init__.py
│       ├── conftest.py          # Pytest config (NEW)
│       ├── test_integration.py  # Integration tests (NEW)
│       └── test_nodes/          # Unit tests
│           ├── __init__.py
│           ├── test_intent_node.py
│           ├── test_priority_node.py
│           ├── test_policy_node.py
│           ├── test_draft_node.py
│           ├── test_validation_node.py
│           └── test_router_node.py
│
├── 📝 Scripts & Examples
│   ├── scripts/                  # Utility scripts
│   │   ├── test_workflow.py     # Integration test script
│   │   ├── dev_server.py        # Dev server (NEW)
│   │   └── setup_model.py       # Model setup (NEW, if needed)
│   └── examples/                 # Usage examples
│       └── sample_requests.json # Sample API requests
│
└── 📦 Build & Deploy (Future)
    ├── Dockerfile               # (FUTURE)
    ├── docker-compose.yml       # (FUTURE)
    └── .github/
        └── workflows/           # CI/CD (FUTURE)
```

---

## 🔄 Migration Steps

### Phase 1: Create New Directory Structure
```bash
# Create new directories
mkdir docs
mkdir docs\notebooks
mkdir tests
mkdir tests\test_nodes
```

### Phase 2: Move Files
1. **Move documentation files:**
   - `summary.md` → `docs/project_summary.md`
   - `Build a Banking AI-Agent.pdf` → `docs/`
   - `Ollama-Pinggy.ipynb` → `docs/notebooks/`

2. **Update all references** in moved files

### Phase 3: Create New Files

#### 3.1 Create `pyproject.toml`
```toml
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "banking-ai-agent"
version = "1.0.0"
description = "AI-powered banking customer support agent"
readme = "README.md"
requires-python = ">=3.10"
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
keywords = ["nlp", "ai", "banking", "fastapi", "ollama"]
license = {text = "MIT"}
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]

dependencies = [
    "fastapi",
    "uvicorn",
    "pydantic",
    "pydantic-settings",
    "python-dotenv",
    "requests",
]

[project.optional-dependencies]
dev = [
    "pytest",
    "pytest-asyncio",
    "black",
    "flake8",
    "mypy",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]

[tool.black]
line-length = 88
target-version = ['py310', 'py311']

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
```

#### 3.2 Create `configs/default.yaml`
```yaml
# Default Application Configuration
app:
  name: "Banking AI-Agent"
  version: "1.0.0"
  debug: false

ollama:
  base_url: "http://localhost:11434"
  model: "gpt-oss:20b"
  timeout: 120

intent_model:
  path: "../../Ex2/models/intent_model/"
  config_path: "../../Ex2/configs/inference.yaml"

workflow:
  validation_enabled: true
  max_tokens: 512
  confidence_threshold: 0.6

logging:
  level: "INFO"
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
```

#### 3.3 Create Documentation Files

**`docs/architecture.md`:**
```markdown
# System Architecture

## Overview
The Banking AI-Agent follows a modular, node-based pipeline architecture...

## Components
1. **Intent Detection Node** - Classifies user queries
2. **Priority Assessment Node** - Determines urgency
3. **Policy Retrieval Node** - Fetches relevant policies
4. **Response Drafting Node** - Generates responses using LLM
5. **Validation Node** - Checks response quality
6. **Router Node** - Decides next action

## Data Flow
[Diagram and detailed explanation]
```

**`docs/api.md`:**
```markdown
# API Documentation

## Base URL
`http://localhost:8000`

## Endpoints

### POST /process
Process a banking query through the AI agent workflow.

**Request Body:**
```json
{
  "query": "I lost my credit card",
  "session_id": "optional-uuid"
}
```

**Response:**
```json
{
  "query": "I lost my credit card",
  "response": "I understand you've lost your card...",
  "trace": {
    "intent": {...},
    "priority": {...},
    "policy": {...},
    "draft": {...},
    "validation": {...},
    "router": {...}
  }
}
```
```

**`docs/setup.md`:**
```markdown
# Setup Guide

## Prerequisites
- Python 3.10+
- Ollama installed and running
- Lab 2 model (if using intent classification)

## Installation Steps
1. Clone repository
2. Create virtual environment
3. Install dependencies
4. Configure environment variables
5. Start Ollama service
6. Run the application
```

#### 3.4 Create Test Structure

**`tests/__init__.py`:**
```python
# Test package initialization
```

**`tests/conftest.py`:**
```python
import pytest
from app.core.schemas import QueryRequest

@pytest.fixture
def sample_query_request():
    return QueryRequest(query="I lost my credit card")

@pytest.fixture
def sample_queries():
    return [
        "What is my balance?",
        "My transfer failed",
        "I lost my card",
        "How do I unblock my account?"
    ]
```

**`tests/test_nodes/test_intent_node.py`:**
```python
import pytest
from app.nodes.intent_node import IntentNode
from app.core.schemas import Priority

def test_intent_node_initialization():
    node = IntentNode()
    assert node is not None

def test_intent_detection_card_lost():
    node = IntentNode()
    result = node.process("I lost my credit card at the mall")
    assert result.intent == "card_lost"
    assert result.confidence > 0.5

def test_intent_detection_balance_inquiry():
    node = IntentNode()
    result = node.process("What is my account balance?")
    assert result.intent == "balance_inquiry"
```

[Similar test files for other nodes...]

### Phase 4: Update Existing Files

#### 4.1 Update `README.md`
Add sections about:
- New project structure
- How to run tests
- Configuration options
- API documentation links

#### 4.2 Update `run.py`
Improve path handling:
```python
import uvicorn
import os
from pathlib import Path

def main():
    """Run the Banking AI-Agent server."""
    # Get project root
    project_root = Path(__file__).parent
    
    # Configuration
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    reload = os.getenv("DEBUG", "false").lower() == "true"
    
    # Run server
    uvicorn.run(
        "app.main:app",
        host=host,
        port=port,
        reload=reload,
        log_level="info"
    )

if __name__ == "__main__":
    main()
```

#### 4.3 Update `scripts/test_workflow.py`
Fix path handling:
```python
import json
import requests
from pathlib import Path

def test_workflow():
    url = "http://localhost:8000/process"
    
    # Get project root
    project_root = Path(__file__).parent.parent
    samples_path = project_root / "examples" / "sample_requests.json"
    
    with open(samples_path, "r") as f:
        samples = json.load(f)
    
    # Rest of the test logic...
```

#### 4.4 Update `.gitignore`
Add patterns for new structure:
```gitignore
# Testing
.pytest_cache/
.coverage
htmlcov/
tests/results/

# Documentation builds
docs/_build/

# Configuration
configs/local.yaml
configs/*.local.yaml

# IDE
.vscode/
.idea/
*.swp
*.swo

# Environment
.env
.venv/
venv/

# Python
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/
```

### Phase 5: Validation & Testing

1. **Verify all imports work** after restructuring
2. **Run existing tests** (if any)
3. **Test the API** with sample requests
4. **Check documentation** links and references
5. **Validate configuration** loading

---

## 📊 Benefits of This Refactoring

### 1. **Professional Structure**
- Follows Python packaging best practices
- Clear separation of concerns
- Industry-standard layout

### 2. **Improved Maintainability**
- Logical file organization
- Easy to locate components
- Clear module boundaries

### 3. **Better Documentation**
- Dedicated docs directory
- Comprehensive guides
- API documentation

### 4. **Enhanced Testing**
- Proper test structure
- Easy to add new tests
- Clear test organization

### 5. **Scalability**
- Easy to add new features
- Clear extension points
- Modular design

### 6. **Team Collaboration**
- Clear structure for team members
- Standard conventions
- Easy onboarding

---

## ⚠️ Potential Issues & Solutions

### Issue 1: Import Path Changes
**Problem:** Relative imports might break after moving files.
**Solution:** Update all imports systematically and test thoroughly.

### Issue 2: Configuration File Locations
**Problem:** Hard-coded paths in settings.
**Solution:** Use environment variables and relative paths from project root.

### Issue 3: External References
**Problem:** Links in documentation might break.
**Solution:** Update all documentation links and verify.

### Issue 4: Git History
**Problem:** File moves might affect git history.
**Solution:** Use `git mv` for moves to preserve history.

---

## 🚀 Implementation Timeline

### Estimated Time: 2-3 hours

1. **Phase 1-2:** Create structure and move files (30 minutes)
2. **Phase 3:** Create new files (1 hour)
3. **Phase 4:** Update existing files (45 minutes)
4. **Phase 5:** Testing and validation (45 minutes)

---

## ✅ Success Criteria

- [ ] All files organized in logical directories
- [ ] No broken imports or references
- [ ] All tests pass
- [ ] API endpoints work correctly
- [ ] Documentation is complete and accurate
- [ ] Configuration loads properly
- [ ] Project can be run without errors

---

## 📞 Next Steps

1. Review and approve this plan
2. Create a backup/branch before starting
3. Execute refactoring step by step
4. Test thoroughly after each phase
5. Update any external documentation/links

---

**Note:** This refactoring maintains all existing functionality while improving the project structure. No features will be lost or changed in behavior.