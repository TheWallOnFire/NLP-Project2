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
        response = requests.post(url, json=payload, timeout=120)
        response.raise_for_status()
        return response.json()["response"]

    def chat(self, messages: List[Dict[str, str]], **kwargs) -> str:
        url = f"{self.base_url}/api/chat"
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
            **kwargs
        }
        response = requests.post(url, json=payload, timeout=120)
        response.raise_for_status()
        return response.json()["message"]["content"]
