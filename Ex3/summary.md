# 📋 Project 3 Summary: Build a Banking AI-Agent

This document provides a concise summary of the requirements, architecture, and objectives for **Project 3: Build a Banking AI-Agent**, based on the course documentation.

---

## 🎯 Project Objective
The goal is to design and implement an **AI agentic workflow** for banking customer support. The system must be capable of:
- Receiving and understanding customer queries.
- Retrieving relevant bank policies or FAQs.
- Drafting professional, context-aware responses.
- Validating the response quality and deciding on the next action (Send, Clarify, or Escalate).

---

## 🏗️ Core Architecture (The Agentic Workflow)
The project requires a modular, node-based pipeline consisting of several mandatory stages:

| Node | Responsibility |
| :--- | :--- |
| **Intent Detection** | Identify the user's goal using the fine-tuned model from Lab 2. |
| **Priority Assessment** | Determine the urgency (Low, Medium, High) and risk level of the query. |
| **Policy Retrieval** | Fetch relevant documentation or FAQ snippets from a knowledge base. |
| **Response Drafting** | Use an LLM to generate a draft reply based on query, intent, and policy. |
| **Validation** | Check if the response is consistent, accurate, and complete. |
| **Escalation/Routing** | Decide whether to reply directly or transfer the case to human support. |

---

## 🛠️ Technical Stack
- **AI Engine**: [Ollama](https://ollama.com/) running **gpt-oss-20b** (or similar open-weight models).
- **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/) to host the agent as a RESTful service.
- **Inference**: High-performance local inference for the specialized intent model.
- **External Access**: [Pinggy](https://pinggy.io/) for tunneling local ports to public URLs (useful for Colab integration).

---

## 📊 Evaluation & Deliverables
The project is evaluated based on:
1.  **Source Code Structure**: Well-organized folders (app, nodes, agents, core) with clear implementation logic.
2.  **Workflow Traceability**: The ability of the orchestrator to log and show intermediate outputs of each node.
3.  **Video Demonstration**: A 2–5 minute recording showing:
    - Execution of the inference script.
    - Processing of multiple example queries.
    - Final output and accuracy obtained on the test set.
4.  **Documentation**: A comprehensive README.md detailing setup, execution, and demonstration links.

---
*Summary generated for the NLP in Industry Course - Project 3.*
