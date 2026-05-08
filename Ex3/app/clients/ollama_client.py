import requests
from typing import List, Dict, Any
from .base import BaseLLMClient
from ..core.settings import settings

class OllamaClient(BaseLLMClient):
    def __init__(self):
        self.base_url = settings.OLLAMA_BASE_URL
        self.model = settings.OLLAMA_MODEL

    def generate(self, prompt: str, **kwargs) -> str:
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            **kwargs
        }
        try:
            # Increased timeout to 300s (5 minutes) for large models
            response = requests.post(url, json=payload, timeout=300)
            response.raise_for_status()
            return response.json()["response"]
        except requests.exceptions.ReadTimeout:
            raise RuntimeError(f"Ollama server timed out after 300s while generating a response with model {self.model}. The model may be too large for the current hardware.")
        except Exception as e:
            raise e

    def chat(self, messages: List[Dict[str, str]], **kwargs) -> str:
        url = f"{self.base_url}/api/chat"
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
            **kwargs
        }
        try:
            # Increased timeout to 300s (5 minutes) for large models
            response = requests.post(url, json=payload, timeout=300)
            response.raise_for_status()
            return response.json()["message"]["content"]
        except requests.exceptions.ReadTimeout:
            raise RuntimeError(f"Ollama server timed out after 300s while chatting with model {self.model}.")
        except Exception as e:
            raise e
