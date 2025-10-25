# Fibonacci Series up to n terms

n = int(input("Enter number of terms: "))

# first two numbers of Fibonacci series
a, b = 0, 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    # update values for next term
    a, b = b, a + b
