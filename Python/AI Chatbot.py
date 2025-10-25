def chatbot():# reused you define it in function sytanx of function is def funname():
    print("🤖 Hello! I'm ChatBot. How can I help you today?")#print(" string 123")
    print("Type 'bye' or 'exit' to end the conversation.\n")# anything "" becomes as string name="arisha"
#while condition
    while True:#chatbot with a condition true
        user_input = input("You:Name ").lower()# input() function input take input from user on prompt
        # string function () .lower case .upper ASCII value A a uniform ArisHa
        #if true   elif always come after if  else last
        if user_input in ['bye', 'exit', 'quit']:# membership operator in
            print("ChatBot: Goodbye! Have a nice day 😊")
            break

        elif "hello" in user_input or "hi" in user_input:# and both comdition true or either true not a=5 b=6 a!=b=true
            print("ChatBot: Hello there! How can I assist you?")

        elif "how are you" in user_input:
            print("ChatBot: I'm just a bunch of code, but thanks for asking! How are you?")

        elif "your name" in user_input:
            print("ChatBot: I'm ChatBot, your friendly AI assistant.")

        elif "help" in user_input:
            print("ChatBot: Sure! I can chat with you or answer simple questions. Try asking something!")

        elif "weather" in user_input:
            print("ChatBot: I'm not connected to live weather data, but it's always sunny in the code world! 😄")

        else:
            print("ChatBot: I'm not sure how to respond to that. Can you ask something else?")

# Run the chatbot
chatbot()
