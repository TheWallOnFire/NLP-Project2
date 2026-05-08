import requests
import json

url = "http://localhost:8000/process"
payload = {"query": "how do I check my balance?"}

try:
    response = requests.post(url, json=payload)
    print(f"Status Code: {response.status_code}")
    print("Response JSON:")
    print(json.dumps(response.json(), indent=2))
except Exception as e:
    print(f"Error: {e}")
