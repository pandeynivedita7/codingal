import numpy as np

# Define data type for structured array
data_type = [
    ('name', 'S15'),     # string of length 15
    ('class', int),
    ('height', float)
]

# Student records
students_details = [# list 
    ('James', 5, 48.5),# tuple
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.10),
    ('Pit', 5, 40.11)
]

# Create structured array
students = np.array(students_details, dtype=data_type)

print("Original array:")
print(students)

print("\nSorted by height:")
print(np.sort(students, order='height'))
