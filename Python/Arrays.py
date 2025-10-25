import array as arr

# create an array
array_num = arr.array('i', [1, 3, 5, 3, 7, 9, 3])# creating (i,[1,2,3,4,5])
print("Original array: "+str(array_num))
#arrayname=array.methodname
# count number of occurences
print("Number of occurrences of the number 3 in the said array: "+str(array_num.count(3)))
array_num.append(34)
array_num.remove(5)
# reverse the array 
array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))