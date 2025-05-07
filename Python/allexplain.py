# building rule based chatbot
import re, random # random number
from colorama import Fore, init

init(autoreset=True):
destination={
    "beaches":["Bali","Maldives","Phuket"],
    "mountains":["Himalays","Swiss Alps","Rocky Mountain"]
}

Jokes=["hi how are you",
"Hope you are fine",
"My day was good"]#list add and deleting data is easy

def normalize(text):# def funname (parameter):
    return(text.strip().lower())
print(Fore.CYAN + "HI how are you")

if Jokes == "yes":
    print(f"hi hoe are you,{destination}")
elif Jokes =="NO":
    print("hello")
else:
    print("Buy")

while False:
    var1=input("Enter your age")
    break
    continues





