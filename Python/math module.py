import math  # importing math module
squareroot=math.sqrt(16)# math.abs(-7) math.pow(2,3)
print(squareroot)


# using ceil and floor function of math module
print('The Floor and Ceiling value of 23.56 are: ' +
      str(math.ceil(23.56)) + ', ' + str(math.floor(23.56)))

x = 10
y = -15

# using copysign function
print('The value of x after copying the sign from y is: ' +
      str(math.copysign(x, y)))# copy sign from 1 variable to another

# using fabs and gcd function
print('Absolute value of -96 and 56 are: ' +
      str(math.fabs(-96)) + ', ' + str(math.fabs(56)))# fabs only positive

print('The GCD of 24 and 56 : ' + str(math.gcd(24, 56)))
