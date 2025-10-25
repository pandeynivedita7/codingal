# Half Pyramid Pattern of Stars
print("Half Pyramid Pattern of Stars (*)")
n = int(input("Enter the number of rows: "))#6
for i in range(n):# rows*
    for j in range(i + 1):# columns
        print("*", end=" ")
        
    print()

