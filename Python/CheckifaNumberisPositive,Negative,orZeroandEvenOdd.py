num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")
