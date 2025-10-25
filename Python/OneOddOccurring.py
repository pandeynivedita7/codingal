def OddOccuring(arr):# use of suntion recall/reuse arr(array list of data)
  res = 0# variable assigned value
  for element in arr:# travel sytanx for var in (range)
    res = res ^ element# bitwise or
  return res

arr = []#list list of element
n = int(input("Enter array size:"))#5
while(n):
  num = int(input("Enter number:"))# how many number 
  arr.append(num)#Add the entered number to the list at end
  n-=1#n=n-1 Decrement n by one; when n reaches zero the loop stops.

print("OddOccuring number is",OddOccuring(arr))#3^5^6^7^8