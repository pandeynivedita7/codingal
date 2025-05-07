import random

# Dictionary of possible responses
responses = {
    "hello": ["Hey there!", "Hi!", "Hello! How can I help you today?"],
    "how are you": ["I'm doing great, thanks!", "Feeling awesome! What about you?", "I'm here to help!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "name": ["I'm your friendly chatbot!", "You can call me ChatBuddy!", "I'm just a bot, but a nice one!"],
    "default": ["Hmm, I'm not sure I understand that.", "Can you rephrase?", "Interesting... tell me more!"]
}

# Function to get a response based on user input
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

# Main chat loop
print("Hello! I'm your friendly chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("Bot:", random.choice(responses["bye"]))
        break
    response = get_response(user_input)
    print("Bot:", response)
