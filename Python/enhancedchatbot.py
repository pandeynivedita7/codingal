import re, random, time
from colorama import Fore, init

# Initialize colorama for colored terminal output
init(autoreset=True)

# Dictionary of travel destinations
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"],
    "historical": ["Rome", "Athens", "Cairo"],
    "adventure": ["Queenstown", "Costa Rica", "Nepal"],
    "desert": ["Sahara", "Dubai", "Thar Desert"]
}

# List of jokes
jokes = [
    "Why don't programmers like nature? Too many bugs! 😂",
    "Why did the computer go to the doctor? Because it had a virus! 🖥️🤒",
    "Why do travelers always feel warm? Because of all their hot spots! 🔥✈️"
]

# Normalize user input by removing extra spaces and converting to lowercase
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

# Match if any keyword is in the user input
def match_keywords(text, keywords):
    return any(re.search(rf"\b{kw}\b", text) for kw in keywords)

# Recommend a travel destination
def recommend():
    print(Fore.CYAN + "TravelBot 🌍: Beaches, mountains, cities, historical, adventure, or desert?")
    preference = normalize_input(input(Fore.YELLOW + "You: "))
    
    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: ✈️ How about visiting {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer = normalize_input(input(Fore.YELLOW + "You: "))

        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome! 🎉 Enjoy your trip to {suggestion}!")
        elif answer == "no":
            print(Fore.RED + "TravelBot: No worries, let me suggest another place!")
            time.sleep(1)
            recommend()
        else:
            print(Fore.RED + "TravelBot: I didn't catch that, let's try again!")
            recommend()
    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have suggestions for that category.")
    
    show_help()

# Offer packing tips
def packing_tips():
    print(Fore.CYAN + "TravelBot 🧳: Where are you traveling?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: For how many days?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"\nTravelBot: Packing tips for {days} days in {location.title()}:")
    print(Fore.GREEN + "✔️ Pack versatile clothes.")
    print(Fore.GREEN + "✔️ Bring chargers/adapters.")
    print(Fore.GREEN + "✔️ Carry a basic first-aid kit.")
    print(Fore.GREEN + "✔️ Check the weather forecast before you go!")

# Tell a random joke
def tell_joke():
    print(Fore.YELLOW + f"TravelBot 🤪: {random.choice(jokes)}")

# Provide mock weather info
def weather_info():
    location = normalize_input(input(Fore.YELLOW + "TravelBot: Which location do you want weather info for? "))
    # Mocked weather response
    weather_mock = random.choice(["sunny ☀️", "rainy 🌧️", "cloudy ☁️", "snowy ❄️", "windy 🌬️"])
    temperature = random.randint(15, 35)
    print(Fore.GREEN + f"TravelBot: The weather in {location.title()} is currently {weather_mock} with {temperature}°C.")

# Show help menu
def show_help():
    print(Fore.MAGENTA + "\n📖 TravelBot Help Menu:")
    print(Fore.GREEN + "- Type 'recommend' to get travel suggestions 🧭")
    print(Fore.GREEN + "- Type 'packing' to get packing tips 🧳")
    print(Fore.GREEN + "- Type 'joke' to hear a travel joke 😄")
    print(Fore.GREEN + "- Type 'weather' to get current weather info 🌦️ (mock)")
    print(Fore.CYAN + "- Type 'exit' or 'bye' to leave the chat 🚪\n")

# Main chatbot loop
def chat():
    print(Fore.CYAN + "👋 Hello! I'm TravelBot, your personal travel assistant.")
    name = input(Fore.YELLOW + "What's your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}! 😄")
    
    show_help()
    
    while True:
        user_input = normalize_input(input(Fore.YELLOW + f"{name}: "))
        
        if match_keywords(user_input, ["recommend", "suggest", "destination"]):
            recommend()
        elif match_keywords(user_input, ["pack", "packing", "bags"]):
            packing_tips()
        elif match_keywords(user_input, ["joke", "funny", "laugh"]):
            tell_joke()
        elif match_keywords(user_input, ["weather", "climate", "temperature"]):
            weather_info()
        elif match_keywords(user_input, ["help", "options", "menu"]):
            show_help()
        elif match_keywords(user_input, ["exit", "bye", "quit"]):
            print(Fore.CYAN + "TravelBot: Safe travels! 🌏 Goodbye! 👋")
            break
        else:
            print(Fore.RED + "TravelBot: Hmm 🤔 I didn't get that. Please type 'help' to see options.")

# Run the chatbot
if __name__ == "__main__":
    chat()
