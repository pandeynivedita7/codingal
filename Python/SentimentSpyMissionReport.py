# Install these first if not done:
# pip install colorama textblob texttable
# python -m textblob.download_corpora

import colorama
from colorama import Fore, Style
from textblob import TextBlob
from texttable import Texttable

# Initialize colorama
colorama.init()

# Welcome screen
print(f"{Fore.CYAN}== Welcome to Sentiment Spy! =={Style.RESET_ALL}")
user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "Mystery Agent"

print(f"\n{Fore.CYAN}Hello Agent {user_name}!")
print("Type a sentence and I will analyze your sentiment using TextBlob.")
print(f"Use the following commands anytime:\n"
      f"{Fore.YELLOW}'history'{Style.RESET_ALL} - View all previous inputs\n"
      f"{Fore.YELLOW}'reset'{Style.RESET_ALL} - Clear all history\n"
      f"{Fore.YELLOW}'exit'{Style.RESET_ALL} - Exit and view final report\n")

# Conversation history as list of tuples
conversation_history = []

# Main loop
while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}⚠️ Please enter some text or a command.{Style.RESET_ALL}")
        continue

    # Exit command
    if user_input.lower() == "exit":
        print(f"\n{Fore.CYAN}🕵️‍♀️ Mission Complete, Agent {user_name}!")
        print(f"{Fore.CYAN}🧾 Final Sentiment Summary:{Style.RESET_ALL}")

        # Count sentiment types
        positive = sum(1 for _, _, s in conversation_history if s == "Positive")
        negative = sum(1 for _, _, s in conversation_history if s == "Negative")
        neutral  = sum(1 for _, _, s in conversation_history if s == "Neutral")
        total = len(conversation_history)

        print(f"{Fore.GREEN}Positive: {positive}")
        print(f"{Fore.RED}Negative: {negative}")
        print(f"{Fore.YELLOW}Neutral : {neutral}")
        print(f"{Fore.CYAN}Total   : {total}{Style.RESET_ALL}")
        print(f"\n{Fore.MAGENTA}Thank you for using Sentiment Spy!{Style.RESET_ALL}")
        break

    # Reset command
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}🔄 All conversation history cleared!{Style.RESET_ALL}")
        continue

    # History command
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}⚠️ No history to show yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}📜 Conversation History:{Style.RESET_ALL}")
            table = Texttable()
            table.add_row(["ID", "Text", "Polarity", "Sentiment"])
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                elif sentiment_type == "Negative":
                    color = Fore.RED
                else:
                    color = Fore.YELLOW
                table.add_row([idx, color + text + Style.RESET_ALL, f"{polarity:.2f}", sentiment_type])
            print(table.draw())
        continue

    # Analyze sentiment
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment_type = "Positive"
        color = Fore.GREEN
    elif polarity < 0:
        sentiment_type = "Negative"
        color = Fore.RED
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW

    print(f"{color}🧠 Sentiment: {sentiment_type} (Polarity: {polarity:.2f}){Style.RESET_ALL}")
    conversation_history.append((user_input, polarity, sentiment_type))
