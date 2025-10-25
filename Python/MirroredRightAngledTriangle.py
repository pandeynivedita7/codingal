rows = int(input("Enter number of rows: "))#5

for i in range(1, rows + 1):#rows
    # Print spaces first
    for j in range(rows - i):# current position 
        print(" ", end="")
    
    # Print stars after spaces
    for k in range(i):
        print("*", end="")
    
    # Move to next line
    print()
