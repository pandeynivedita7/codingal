import requests

API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
headers = {"Authorization": "Bearer YOUR_API_KEY"}

data = {"inputs": "I love learning about APIs!"}

response = requests.post(API_URL, headers=headers, json=data)
print(response.json())


import requests

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": "Bearer YOUR_API_KEY"}  # Replace with your token

data = {
    "inputs": "Once upon a time",
    "parameters": {"max_length": 50}
}

response = requests.post(API_URL, headers=headers, json=data)
result = response.json()

print(result[0]["generated_text"])


import requests

API_URL = "https://api-inference.huggingface.co/models/google/vit-base-patch16-224"
headers = {"Authorization": "Bearer YOUR_API_KEY"}

with open("cat.jpg", "rb") as f:
    response = requests.post(API_URL, headers=headers, data=f)

print(response.json())
