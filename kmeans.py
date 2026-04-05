import requests

def call_gpt(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": "Bearer sk-proj-1234567890",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

def main():
    prompt = "Hello, how are you?"
    response = call_gpt(prompt)
    print(response)

if __name__ == "__main__":
    main()