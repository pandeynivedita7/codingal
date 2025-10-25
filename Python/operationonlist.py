lst = ['Apple', 'Guava', 'Mango', 'Banana', 'Kiwi']

print("Length of list:", len(lst))# length len(listname) 5
print("First Element:", lst[0])# apple
print("Last Element:", lst[-1])# kiwi

lst.append('Papaya')
print("Updated List :", lst)

lst.remove('Guava')
print("Updated List :", lst)

lst.sort()
print("Sorted List:", lst)

lst.pop(1)
print("Updated List :", lst)# 1st element of list

lst.reverse()
print("Reversed List :", lst)

print("Multiplication on List :", lst * 2)
# 2 operation in list 
# 1 + that acts like join lis 1 + list1 with list2 list3=list1+list2
#* muliplication repeation *2
# sublist from the list this method is called as slicing
# listname[s:e]

lst = lst[:4]
#lst=lst[4:]
print("Sliced List :", lst)

lst.clear()
print("Updated List :", lst)
#lst.delete()
