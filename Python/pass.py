# Iterate through numbers 0 to 9
for x in range(10):
    if x % 20 == 0:  # condition 1
        print("twist")
    elif x % 15 == 0:  # condition 2 5
        pass  # do nothing
    elif x % 5 == 0:  # condition 3
        print("fizz")
    elif x % 3 == 0:  # condition 4
        print("buzz")
    else:  # condition 5
        print(x)
