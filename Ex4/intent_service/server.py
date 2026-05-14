import grpc
from concurrent import futures
import time
import requests
import json
import os

import intent_service_pb2
import intent_service_pb2_grpc

class IntentServiceServicer(intent_service_pb2_grpc.IntentServiceServicer):
    def __init__(self):
        self.ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        self.model_name = os.getenv("INTENT_MODEL_NAME", "gpt-oss:20b")
        print(f"IntentService initialized with Ollama at {self.ollama_url} using model {self.model_name}")

    def IntentRecognizer(self, request, context):
        message = request.message
        print(f"Received message: {message}")

        prompt = f"""
        You are a banking intent classifier. Classify the following user message into one of these intents:
        - check_balance
        - transfer_funds
        - pay_bills
        - view_transactions
        - customer_support
        - unknown

        User message: "{message}"

        Return ONLY a JSON object with the following fields:
        "intent": the classified intent
        "confidence": a float between 0 and 1
        "reason": a brief explanation for the classification

        Example:
        {{"intent": "check_balance", "confidence": 0.95, "reason": "User is asking for their account balance."}}
        """

        try:
            response = requests.post(
                f"{self.ollama_url}/api/generate",
                json={
                    "model": self.model_name,
                    "prompt": prompt,
                    "stream": False,
                    "format": "json"
                },
                timeout=30
            )
            response.raise_for_status()
            result = response.json()
            
            # Parse the response content
            content = result.get("response", "{}")
            data = json.loads(content)
            
            return intent_service_pb2.IntentResponse(
                intent=data.get("intent", "unknown"),
                confidence=float(data.get("confidence", 0.0)),
                reason=data.get("reason", "No reason provided")
            )
        except Exception as e:
            print(f"Error calling Ollama: {e}")
            return intent_service_pb2.IntentResponse(
                intent="unknown",
                confidence=0.0,
                reason=f"Error: {str(e)}"
            )

def serve():
    port = os.getenv("GRPC_PORT", "50051")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    intent_service_pb2_grpc.add_IntentServiceServicer_to_server(IntentServiceServicer(), server)
    server.add_insecure_port(f'[::]:{port}')
    print(f"Starting gRPC server on port {port}...")
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
