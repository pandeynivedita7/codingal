

fruits=["apple","pear","graphs","mango"]# list use 1 ordered 2 mutable change 3 duplicate
print(fruits)
print(fruits[1])
print(len(fruits))# ( method len function 3 user defined system and defualt)
fruits[1]="orange"
print(fruits)#. operator is used to access something
fruits.remove("mango")
print(fruits)

fruits = ["apple", "banana", "cherry"]

print(fruits[0])     # First item
print(fruits[-1])    # Last item
print(fruits[1:])    # Slice from index 1 to end

fruits[1] = "orange"  # Change banana to orange

fruits.append("kiwi")       # Add at end
fruits.insert(1, "grapes")  # Insert at index 1

fruits.remove("apple")  # Remove by value
fruits.pop()            # Remove last item
fruits.pop(0)           # Remove by index
del fruits[1]           # Delete by index

fruits = ["banana", "apple", "cherry"]
fruits.sort()          # Sort ascending
fruits.reverse()       # Reverse order
fruits.clear()         # Remove all elements

print(len(fruits))     # Number of elements
print("apple" in fruits)  # Check existence

squares = [x**2 for x in range(5)]

copy_list = fruits.copy()

list1 = [1, 2]
list2 = [3, 4]
list1.extend(list2)

list1 = [1, 2]
list2 = [3, 4]
list1.extend(list2)

fruits = ["apple", "banana", "apple"]
print(fruits.count("apple"))  # Output: 2

print(fruits.index("banana"))