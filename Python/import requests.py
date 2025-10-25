import requests
from config import HF_API_KEY

def classify_text(text):
    API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"# hugging face API
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}# dict{Key :values}
    payload = {"inputs": text}# input json body

    response = requests.post(API_URL, headers=headers, json=payload)# http post resopnse 
    return response.json()

if __name__ == "__main__":# main function
    sample_text = "I love using Hugging Face APIs!"#classify text
    result = classify_text(sample_text)
    print(result)
