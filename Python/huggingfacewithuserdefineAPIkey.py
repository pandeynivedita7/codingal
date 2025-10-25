import requests

def sentiment_analysis(text, api_key):#define function reuse
    # Define Hugging Face API endpoint for sentiment analysis
    api_url = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"

    # Set up headers with your Hugging Face API key
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    # Create the payload
    payload = {
        "inputs": text
    }

    # Send the POST request to the Hugging Face API
    response = requests.post(api_url, headers=headers, json=payload)

    # Check the response status
    if response.status_code == 200:
        result = response.json()
        label = result[0]['label']
        score = result[0]['score']
        print(f"\nSentiment: {label}\nConfidence Score: {score:.4f}")
    else:
        print(f"\nError: {response.status_code}\nDetails: {response.text}")

# ------------------------------
# 🔵 Run the sentiment analysis
# ------------------------------
if __name__ == "__main__":
    user_input = input("Enter text for sentiment analysis: ")
    user_api_key = input("Enter your Hugging Face API key: ")
    
    sentiment_analysis(user_input, user_api_key)
