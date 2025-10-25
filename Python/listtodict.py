def test(lst):# function reused 
    result = {}# empty dict
    for item in lst: # for var in range lst
        result[item[0]] = item[1:]#
    return result

students = [# list within the list is list converts list to dict
    [1, 'Jean Castro', 'V'],
    [2, 'Lula Powell', 'V'],
    [3, 'Brian Howell', 'VI'],
    [4, 'Lynne Foster', 'VI'],
    [5, 'Zachary Simon', 'VII']
]

print("\nOriginal list of lists:")
print(students)

print("\nConverted lists to a dictionary:")
print(test(students))
