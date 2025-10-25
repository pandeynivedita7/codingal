# Example 1: Relational operator '!='
a = 10
b = 12
c = 12
#
print(a != b)  # True
print(b != c)  # False

# Example 2: Comparing strings
a = "nivedita"# its is string
b = "Nivedita"#" string"  ASCII value number which are different for a A

if a != b:#True
    print(a, 'and', b, 'are different.')

# Example 3: Logical comparison with boolean values
a = 4
b = 5

if (a == 1) != (b == 5):  # False!=true =>True=true
    print('Hello')

# Example 4: Check if a number is odd or even using input
a = int(input("Enter a number: "))# input interger
# 2
if a % 2 != 0:#0 !=0 7=0 false
    print(a, "is not an even number.")
else:
    print(a, "is an even number.")
