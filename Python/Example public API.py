import requests

# Step 1: Choose a public API endpoint
url = "https://api.publicapis.org/entries"  # Example public API

# Step 2: Send a GET request
response = requests.get(url)

# Step 3: Check for successful response
if response.status_code == 200:
    data = response.json()  # Convert JSON response to Python dictionary
    print("API Data Retrieved Successfully!")
    print(data)
else:
    print(f"Error fetching data. Status Code: {response.status_code}")
