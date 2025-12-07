import numpy as np

# Create first array: 0–8 reshaped to 3×3
a = np.arange(9, dtype=np.float_).reshape(3, 3)#0-8
#[[0. 1. 2.3 4 5 6 7 8]]     [0 1 2][3 4 5][6 7 8]
print('First array:')
print(a)
print('\n')

# Create second array
b = np.array([10, 10, 10])
print('Second array:')
print(b)
print('\n')

print('Add the two arrays:')
print(np.add(a, b))#[0+10 1+10 2+10]=[10 11 12 ]
#[3+10 4+10 5+10]=[13 14 15]\ [6+10 7+10 8+10]=[16 17 18]

print('\n')

print('Subtract the two arrays:')
print(np.subtract(a, b))
print('\n')

print('Multiply the two arrays:')
print(np.multiply(a, b))
print('\n')

print('Divide the two arrays:')
print(np.divide(a, b))
print('\n')
