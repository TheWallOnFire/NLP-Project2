import json
import requests
import time

def test_workflow():
    url = "http://localhost:8000/process"
    
    # Load sample requests
    with open("examples/sample_requests.json", "r") as f:
        samples = json.load(f)
        
    print(f"🚀 Starting test for {len(samples)} samples...\n")
    
    for sample in samples:
        query = sample["query"]
        print(f"📝 Query: {query}")
        
        try:
            response = requests.post(url, json={"query": query}, timeout=150)
            response.raise_for_status()
            data = response.json()
            
            print(f"🎯 Intent: {data['trace']['intent']['intent']} (Expected: {sample['intent']})")
            print(f"⚖️ Priority: {data['trace']['priority']['level']}")
            print(f"🤖 Response: {data['response']}")
            print(f"🚦 Decision: {data['trace']['router']['decision']}")
            print("-" * 50)
            
        except Exception as e:
            print(f"❌ Error processing query: {e}")
            print("-" * 50)
            
        time.sleep(1)

if __name__ == "__main__":
    test_workflow()
