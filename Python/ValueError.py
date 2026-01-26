# using a try and except
try:# test
    number = int(input("Enter a number: "))
    print("The number entered is", number)# ahmed

# using ValueError
except ValueError as ex:
    print("Exception:", ex)
