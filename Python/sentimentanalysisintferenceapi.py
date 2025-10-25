import requests
from config import HF_API_Key   # Make sure you have a config.py file with HF_API_KEY = "your_api_token"

def classify_text(text):
    API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
    headers = {"Authorization": f"Bearer {HF_API_Key}"}
    payload = {"inputs": text}

    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

if __name__ == "__main__":
    sample_text = "I love using Hugging Face APIs!"
    result = classify_text(sample_text)
    print(result)
