# Square it Out! - Simple Program

# Step 1: Take input from user
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

# Step 2: Create empty lists to store values
squares = []       # all squares
odd_squares = []   # only odd squares
even_squares = []  # only even squares

# Step 3: Generate squares and separate odd/even
for n in range(start, end + 1):
    sq = n * n   # square of the number
    squares.append(sq)
    if sq % 2 == 0:
        even_squares.append(sq)
    else:
        odd_squares.append(sq)

# Step 4: Display results
print("\nSquares between", start, "and", end, ":", squares)
print("Odd Squares:", odd_squares)
print("Even Squares:", even_squares)
