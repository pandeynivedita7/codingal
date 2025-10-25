a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if a > c:
        print("Largest is:", a)
    else:
        print("Largest is:", c)
else:
    if b > c:
        print("Largest is:", b)
    else:
        print("Largest is:", c)
