# Greet the user
print("Hello! I am an AI Bot. What's your name? : ")

# Get user input
name = input()
age=int(input("Enter your age"))

# Respond to the user's name
print(f"Nice to meet you, {name}!")
print(f"Your age is,{age} ")

# Ask a question
print("How are you feeling today? (good/bad/worst) : ")
mood = input().lower()#lower case .lower()

# Use conditional statements to respond based on input
if mood == "good":# == comparsion true and false = and == = assigning == compare if condition statement
    print("I'm glad to hear that!")#if true condition else false multiple true/condition if elif else
elif mood == "bad":
    print("I'm sorry to hear that. Hope things get better soon.")
elif mood == "worst":
    print("feeling low")
else:# false
    print("I see. Sometimes it's hard to put feelings into words.")

# End the conversation
print(f"It was nice chatting with you {name}. Goodbye!")
print(mood)
