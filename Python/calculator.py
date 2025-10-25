def add(P, Q):
    # This function is used for adding two numbers
    return P + Q
# def funnmae(parameter): sytanx

def subtract(P, Q):
    # This function is used for subtracting two numbers
    return P - Q

def multiply(P, Q):
    # This function is used for multiplying two numbers
    return P * Q

def divide(P, Q):
    # This function is used for dividing two numbers
    return P / Q

# Now we will take inputs from the user
print("Please select the operation.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")# print("1234")
print("d. Divide")#// floor division % modulus

choice = input("Please enter choice (a/ b/ c/ d): ")# var=input( string)

num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))

if choice == 'a':# comparsion operator # if true
    print(num_1, "+", num_2, "=", add(num_1, num_2))#+add and connection

elif choice == 'b':#condition elif mulitply condition
    print(num_1, "-", num_2, "=", subtract(num_1, num_2))

elif choice == 'c':
    print(num_1, "*", num_2, "=", multiply(num_1, num_2))

elif choice == 'd':
    print(num_1, "/", num_2, "=", divide(num_1, num_2))

else:# false
    print("This is an invalid input")
