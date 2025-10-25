valid = False
while not valid:  # using nested while loop True
    try:
        n = int(input("Enter a number: "))
        # enter an even number
        while n % 2 == 0:# while problem
            print("bye")
            valid = True
    except ValueError:
        print("Invalid")
