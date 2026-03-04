try:
    # Taking input from user
    num = int(input("Enter a number: "))

    # Manually raising an exception
    if num < 0:
        raise ValueError("Number cannot be negative")

    result = 10 / num
    print("Result:", result)

except ValueError as ve:
    print("ValueError occurred:", ve)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

except Exception as e:
    print("Some other error occurred:", e)

finally:
    print("Execution completed (finally block always runs)")