# Diamond Number Pattern
rowSize = int(input("Enter the number of rows: "))

# Calculate half of the rows
if rowSize % 2 == 0:
    halfDiamRow = rowSize // 2# even equally
else:
    halfDiamRow = (rowSize // 2) + 1# upper half +1

space = halfDiamRow - 1

# Upper part
for i in range(1, halfDiamRow + 1):# number row
    for j in range(1, space + 1):# space column
        print(" ", end=" ")
    space -= 1# SPace=space-1
    num = 1
    for j in range(2 * i - 1):
        print(num, end=" ")
        num += 1
    print()

# Lower part
space = 1
for i in range(1, halfDiamRow):
    for j in range(1, space + 1):
        print(" ", end=" ")
    space += 1
    num = 1
    for j in range(2 * (halfDiamRow - i) - 1):
        print(num, end=" ")
        num += 1
    print()

