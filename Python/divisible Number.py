print("Enter a Number (Numerator): ")
num = int(input())# put a number

print("Enter a Number (Denominator): ")
numd = int(input())# again a number 

if num % numd == 0:# % rest == compare
    print("\n" + str(num) + " is divisible by " + str(numd))#+ operator acts like string operator where you join the string
else:
    print("\n" + str(num) + " is not divisible by " + str(numd))
    
# \n for new line
#%d space + 2 operation 1 is addition and other is string cont  % reminder == comparsion true or false
#/you already now that you have to take int not float
#int(num)
#str(num)