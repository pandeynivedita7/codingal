# a chat where computer is talking with you and asking about your mood
# Greet the user
print("Hello! I am AI Bot. What's your name? : ")

# Get user input
name = input()#hud HUd this different age,colour and adress

# Respond to the user's name
print(f"Nice to meet you, {name}!")# print("",varname)

# Ask a question
print("How are you feeling today? (good/bad) : ")
mood = input().lower()# string function lower lowercase upper case len length of char 

# Use conditional statements to respond based on input
if mood == "good":# == is comparsion(TRue/false) =assignment operator
    print("I'm glad to hear that!")# very good and ver bad
elif mood == "bad":#if True else False if elif else
    print("I'm sorry to hear that. Hope things get better soon.")
else:# good/bad
    print("I see. Sometimes it's hard to put feelings into words.")

# End the conversation
print(f"It was nice chatting with you {name}. Goodbye!")
# for computer a-z are not alphabets they are ascii value