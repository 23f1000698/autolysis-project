import requests

AIPROXY_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjEwMDA2OThAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.MKsEq0u8VL9-Iosnud3wj-16sE2GQqVVhN9ESUoAwTg"
AI_PROXY_BASE_URL = "https://aiproxy.sanand.workers.dev/openai"

headers = {
    "Authorization": f"Bearer {AIPROXY_TOKEN}",
    "Content-Type": "application/json"
}

def test_api():
    if not AIPROXY_TOKEN:
        print("Error: AIPROXY_TOKEN is not set!")
        return

    # Test chat completion with GPT-4o-Mini
    chat_endpoint = f"{AI_PROXY_BASE_URL}/v1/chat/completions"
    payload = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": "What is 2 + 2?"}]
    }
    
    try:
        response = requests.post(chat_endpoint, headers=headers, json=payload)
        print(f"Status: {response.status_code}")
        print("Response:", response.json())
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_api()