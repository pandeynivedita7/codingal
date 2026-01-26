valid = False
while not valid:  # using nested while loop True
    try:# using try and except block use try test the code
        n = int(input("Enter a number: "))
        # enter an even number
        while n % 2 == 0:# while problem # n=4 4%2==0 true
            print("bye")# even number
            valid = True# exit from the loop infinte loop
    except ValueError:
        print("Invalid")# problem it will continue to execute until till the condition is true infinite loop
