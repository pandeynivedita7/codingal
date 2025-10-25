# Greet the user
print("Hello!** I am AI Bot. What's your name? : ")
#print("NIvedita welcomes you for the class 123")
#print(5+6,7*6,9/9)
#age=input("what is your age")#3 types of function 1 user define def funname(paramtere) 2 system fun() input() len() constant
# container variable reuse
#( function())
# Get user input
name = input()

# Respond to the user's name
print("Nice to meet you",name)
#print("your name is",name)

# Ask a question
print("How are you feeling today? (good/bad) : ")# char ASCII value A a is different
mood = input().upper() #Good this is different compare to good G and g have different ASCII value 

# Use conditional statements to respond based on input
if mood == "good":# if True
    print("I'm glad to hear that!")
elif mood == "bad":#
    print("I'm sorry to hear that. Hope things get better soon.")
else:# false
    print("I see. Sometimes it's hard to put feelings into words.")

# End the conversation
print(f"It was nice chatting with you {name}. Goodbye!")
