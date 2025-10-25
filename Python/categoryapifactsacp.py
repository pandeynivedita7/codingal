import requests

BASE_URL = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en&category="

def get_fact(category):
    url = BASE_URL + category
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"💡 {category.capitalize()} Fact: {data['text']}\n")
    else:
        print("⚠️ Could not fetch fact for this category.")

while True:
    user_input = input("Enter a category (technology, science, history) or 'q' to quit: ").lower()
    if user_input == 'q':
        break
    get_fact(user_input)