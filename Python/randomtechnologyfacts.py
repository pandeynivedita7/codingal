import requests

# Technology category fact endpoint
url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en&category=technology"

# Function to fetch and display a random technology-related fact
def get_random_technology_fact():
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        print(f"\n💡 Did you know? {fact_data['text']}\n")
    else:
        print("⚠️ Failed to fetch fact")

# Main loop to interact with the user
while True:
    user_input = input("👉 Press Enter to get a random technology fact or type 'q' to quit: ")
    if user_input.lower() == 'q':
        print("👋 Goodbye!")
        break
    get_random_technology_fact()
