# Creating a set
my_set = {1, 2, 2, 3, 4, 4, 4}
print("Set:", my_set)  # duplicates will be removed

# Adding an element to the set
my_set.add(5)# add is a method that adds value to a give set
print("Updated Set:", my_set)
# my_set={1,3,4,5}
# Creating two sets for operations
set1 = my_set
set2 = {2, 4, 4, 6}#{2,4,6}

print("\nSet 1:", set1)# 1,2,3,4,5
print("Set 2:", set2)#2,4,6

# Difference remove comman
print("Difference:")
print(set1.difference(set2))

print(set2.difference(set1))

# Symmetric Difference
print("Symmetric Difference:")
print(set1.symmetric_difference(set2))
