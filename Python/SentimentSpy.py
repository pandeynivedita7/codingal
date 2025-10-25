import colorama # coloured 
from colorama import Fore, Style# fore text colour and style 
from textblob import TextBlob# sentiment analysis Pre trained model
from texttable import Texttable# textual data table 

# Initialize colorama for colored output
colorama.init()# Prepares colorama to format colored text on supported terminals

# Begin: Start of the program
print(f"{Fore.CYAN}== Welcome to Sentiment Spy! =={Style.RESET_ALL}")#. access 

user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip()# remove whitespace of string
if not user_name:#true not is an membership
    user_name = "Mystery Agent"  # Fallback if user doesn't provide name {}

# Store conversation as list of tuples: (text, polarity, sentiment_type)
conversation_history = []# [] () [] list modified and () tuple fixed 

print(f"\n{Fore.CYAN}Hello Agent {user_name}!")
print("Type a sentence and I will analyze your sentiment using TextBlob.")
print(f"Type {Fore.YELLOW}'reset'{Style.RESET_ALL}, {Fore.YELLOW}'history'{Style.RESET_ALL}, or {Fore.YELLOW}'exit'{Style.RESET_ALL} to quit.\n")

while True:# while is condition/loop
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()
        
    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue# continue and break

    # Exit command
    if user_input.lower() == "exit":#ASCII
        print(f"{Fore.CYAN}👋 Exiting Sentiment Spy. Farewell, Agent {user_name}! 👋{Style.RESET_ALL}")
        break

    # Reset conversation history
    elif user_input.lower() == "reset":
        conversation_history.clear()# history clear()
        print(f"{Fore.CYAN}🔄 All conversation history cleared!{Style.RESET_ALL}")
        continue

    # Show history
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}⚠️ No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}📜 Conversation History:{Style.RESET_ALL}")
            table = Texttable()
            table.add_row(["ID", "Text", "Polarity", "Sentiment"])
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                # Choose color
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
