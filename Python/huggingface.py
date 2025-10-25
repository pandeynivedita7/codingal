import requests
from config import hf_read_apikey

def classify_text(text):
    API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
    headers = {"Authorization": f"Bearer {hf_read_apikey}"}
    payload = {"inputs": text}

    response = requests.post(API_URL, headers=headers, json=payload)#json response

    print("Status Code:", response.status_code)
    print("Raw Response:", response.text)

    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        return {"error": "Invalid JSON response", "response_text": response.text}

if __name__ == "__main__":# main function
    sample_text = "I love using Hugging Face APIs!"#classify text
    result = classify_text(sample_text)
    print(result)

#pre trained BERT sentiment analysis GPT probabilities 