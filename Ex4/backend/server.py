from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import grpc
import os
import requests
import json

import intent_service_pb2
import intent_service_pb2_grpc

app = FastAPI(title="Banking AI-Agent Backend")

class MessageRequest(BaseModel):
    message: str

class ClassificationResponse(BaseModel):
    intent: str
    confidence: float
    reason: str
    response: str

class Backend:
    def __init__(self):
        self.intent_service_host = os.getenv("INTENT_SERVICE_HOST", "intent-service")
        self.intent_service_port = os.getenv("INTENT_SERVICE_PORT", "50051")
        self.ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        self.model_name = os.getenv("INTENT_MODEL_NAME", "gpt-oss:20b")
        
        self.channel = grpc.insecure_channel(f"{self.intent_service_host}:{self.intent_service_port}")
        self.stub = intent_service_pb2_grpc.IntentServiceStub(self.channel)

    def get_intent(self, message: str):
        try:
            request = intent_service_pb2.IntentRequest(message=message)
            response = self.stub.IntentRecognizer(request)
            return response
        except Exception as e:
            print(f"Error calling Intent Service: {e}")
            return None

    def generate_response(self, message: str, intent: str):
        prompt = f"""
        You are a helpful banking assistant. The user said: "{message}"
        The detected intent is: "{intent}"

        Generate a friendly and helpful response to the user based on this intent.
        If the intent is 'check_balance', tell them how to check it or ask for account info.
        If 'transfer_funds', guide them to the transfer page.
        If 'unknown', ask for clarification.
        
        Keep it concise and professional.
        """
        try:
            response = requests.post(
                f"{self.ollama_url}/api/generate",
                json={
                    "model": self.model_name,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=30
            )
            response.raise_for_status()
            return response.json().get("response", "I'm sorry, I couldn't generate a response.")
        except Exception as e:
            print(f"Error calling Ollama for response: {e}")
            return "I'm having trouble connecting to my brain right now. Please try again later."

backend = Backend()

@app.post("/classify", response_model=ClassificationResponse)
async def classify_message(req: MessageRequest):
    intent_data = backend.get_intent(req.message)
    if not intent_data:
        raise HTTPException(status_code=500, detail="Could not contact Intent Service")
    
    agent_response = backend.generate_response(req.message, intent_data.intent)
    
    return {
        "intent": intent_data.intent,
        "confidence": intent_data.confidence,
        "reason": intent_data.reason,
        "response": agent_response
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
