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
