# create class
class IOString():#input output string

	# constructor to set default value
    def __init__(self):#behaviour
        self.str1 = ""# empty string

	# function to get input from user
    def get_String(self):# inbuild class IOString,inbuild gettter and setter get to take input set_put input some variable are private __abc private and you cant chaneg the value
        self.str1 = input("Enter String : ")

	# function to print the string in upper case
    def print_String(self):
        print("Result is :", self.str1.upper())
        print("Result is :", self.str1.lower())

# Object creation
str1 = IOString()

# Call functions
str1.get_String()
str1.print_String()
# upper lower len isupper islower son on
#string function means i am doong string operation
#upper or lower case #ASCII value A a as different ASCII 
#getter and setter 