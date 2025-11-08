# Program: Demonstrating All List Operations in Python

# 1. List Creation
fruits = ['apple', 'banana', 'cherry', 'date']
print("Original list:", fruits)

# 2. Accessing Elements
print("\nAccessing Elements:")
print("First element:", fruits[0])
print("Last element:", fruits[-1])

# 3. Updating Elements
fruits[1] = 'blueberry'
print("\nAfter updating second element:", fruits)

# 4. Adding Elements
print("\nAdding Elements:")
fruits.append('elderberry')         # Add at end
print("After append:", fruits)
fruits.insert(2, 'kiwi')           # Insert at index
print("After insert:", fruits)
fruits.extend(['fig', 'grape'])    # Add multiple
print("After extend:", fruits)

# 5. Removing Elements
print("\nRemoving Elements:")
fruits.remove('date')              # Remove by value
print("After remove:", fruits)
popped_item = fruits.pop(3)        # Remove by index
print(f"After pop (removed '{popped_item}'):", fruits)
del fruits[0]                      # Delete by index
print("After del:", fruits)
fruits.clear()                     # Remove all
print("After clear:", fruits)

# 6. Re-create for further operations
fruits = ['apple', 'banana', 'cherry', 'date', 'apple']

# 7. Searching Elements
print("\nSearching Elements:")
print("Index of 'cherry':", fruits.index('cherry'))
print("Count of 'apple':", fruits.count('apple'))

# 8. Sorting and Reversing
print("\nSorting and Reversing:")
fruits.sort()
print("Sorted list:", fruits)
fruits.reverse()
print("Reversed list:", fruits)

# 9. Copying a List
print("\nCopying a List:")
copy_list = fruits.copy()
print("Copied list:", copy_list)

# 10. Slicing
print("\nSlicing:")
print("First three elements:", fruits[:3])
print("Last two elements:", fruits[-2:])

# 11. Concatenation and Repetition
print("\nConcatenation and Repetition:")
more_fruits = ['mango', 'orange']
combined = fruits + more_fruits
print("Concatenated list:", combined)
print("Repeated list:", fruits * 2)

# 12. Nested Lists
print("\nNested List Example:")
nested = [fruits, more_fruits]
print("Nested list:", nested)
print("Accessing nested element:", nested[1][0])
