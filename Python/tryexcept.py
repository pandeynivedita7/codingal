try:
    x = int(input("Enter a number: "))
    y = 10 / x
    print("Result:", y)
except ZeroDivisionError:
    print("Error: division by zero")
except ValueError:
    print("Error: invalid input")
finally:
    print("End of program")
