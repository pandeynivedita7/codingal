import colorama #library
from colorama import Fore, Style
#from textblob import Textblob

colorama.init()
print(f"{Fore.YELLOW}??????????? welcome dear{Style.DIM}")
age=input(f"{Fore.GREEN}Please Enter your name{Style.RESET_ALL}")
print(f"{Fore.GREEN}????????????? Welcome sir{Style.RESET_ALL}")
user_name=input(f"{Fore.MAGENTA}Please Enter your name:{Style.RESET_ALL}").strip()
history= []# container store things
print(f"{Fore.YELLOW}'reset'{Fore.CYAN},{Fore.YELLOW}'History'{Fore.CYAN}"f"or{Fore.YELLOW}'exit'{Fore.CYAN} to quit.{Style.RESET_ALL} \n")
while True:# condtion While
    user_input=input(f"{Fore.GREEN}>>{Style.RESET_ALL}").strip()
    #break
    #continue

    if not user_input:
        print(f"{Fore.RED} PLease enter some command.{Style.RESET_ALL}")
        continue



