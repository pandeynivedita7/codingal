def swap(a,b):
  a = a^b
  b = a^b
  a = a^b
  print("After swapping: a =",a,"and b =",b)

def swap2(a,b):
  a = (a&b)+(a|b)
  b = a+(~b)+1
  a = a+(~b)+1
  print("After swapping: a =",a,"and b =",b)

swap(10,20)
swap2(10,20)
"""I'll explain both swapping methods step by step.
Method 1: XOR Swap (swap function)
Initial values: a = 10, b = 20
Step 1: a = a^b

Binary: 10 = 1010, 20 = 10100
XOR operation: 1010 ^ 10100 = 11110 (30 in decimal)
Now: a = 30, b = 20

Step 2: b = a^b

b = 30 ^ 20
Binary: 11110 ^ 10100 = 01010 (10 in decimal)
Now: a = 30, b = 10 ✓ (b now has original value of a)

Step 3: a = a^b

a = 30 ^ 10
Binary: 11110 ^ 01010 = 10100 (20 in decimal)
Now: a = 20, b = 10 ✓ (a now has original value of b)

Output: After swapping: a = 20 and b = 10
Why XOR works:

XOR has the property: x ^ y ^ y = x
After step 1: a = a^b
Step 2: b = (a^b)^b = a (cancels out the b)
Step 3: a = (a^b)^a = b (cancels out the original a)


Method 2: Arithmetic Swap (swap2 function)
Initial values: a = 10, b = 20
Step 1: a = (a&b)+(a|b)

a&b (AND): 1010 & 10100 = 00000 (0)
a|b (OR): 1010 | 10100 = 11110 (30)
a = 0 + 30 = 30
Now: a = 30, b = 20

Note: (a&b)+(a|b) effectively computes a + b
Step 2: b = a+(~b)+1

~b (NOT of 20): Flips all bits (results in -21 in two's complement)
(~b)+1 = -b (two's complement negation)
b = 30 + (-20) = 10
Now: a = 30, b = 10 ✓

Step 3: a = a+(~b)+1

~b (NOT of 10): Results in -11 in two's complement
(~b)+1 = -b = -10
a = 30 + (-10) = 20
Now: a = 20, b = 10 ✓

Output: After swapping: a = 20 and b = 10
Why this works:

Step 1: Store sum = a + b in variable a
Step 2: b = sum - b = a (gets original a)
Step 3: a = sum - b = b (gets original b, since b now holds original a)


Key Differences:
FeatureXOR MethodArithmetic MethodOperationsBitwise XORBitwise AND/OR + arithmeticEfficiencyMore efficientSlightly more complexRiskNone for integersCan overflow with large numbersReadabilityLess intuitiveEven less intuitive"""