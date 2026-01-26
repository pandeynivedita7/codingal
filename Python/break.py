# Take user input
a = input("Enter a word: ")#apple

# Program to check for 'A' using break
for i in a:  # iterate through each character travesal
    if (i == 'A' or i=='a'):  # condition 1
        print("A is found")  # display result
        break  # break statement
else:
    print("A not found")  # display result
    # or choice  and both condition true not opposite
