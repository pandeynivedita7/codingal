import requests# request library to make http request

# Hugging Face API URL for sentiment analysis
api_url = "https://api-inference.huggingface.co/models/distilbert-base-uncased"

# Replace with your Hugging Face API token
headers = {
    "Authorization": "Bearer YOUR_API_KEY_HERE"
}# key and values

# Sample text for sentiment analysis
text = "I love this movie! It was fantastic."

# Send POST request to the Hugging Face API
response = requests.post(api_url, headers=headers, json={"inputs": text})#JSON sent text analysed

if response.status_code == 200:
    # Parse the response JSON
    result = response.json()# list group madified
    print(f"Sentiment: {result[0][0]['label']} with confidence score: {result[0][0]['score']}")# +ve,-ve and netural
else:#[[{'label': 'POSITIVE', 'score': 0.99}]]
    print(f"Error: {response.status_code}")
