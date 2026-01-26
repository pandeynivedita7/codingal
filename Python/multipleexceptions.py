
try:
    num1, num2 = eval(input("Enter two numbers, separated by a comma : "))# eval a function used to evaluate the expression check a exsspression is valid or not a+b 4+6 +46 
    result = num1 / num2
    print("Result is", result)

# using multiple except block for different type of error
except ZeroDivisionError:
    print("Division by zero is error !!")

except SyntaxError:
    print("Comma is missing. Enter numbers separated by comma like this 1, 2")# eval a,b,d

except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")
