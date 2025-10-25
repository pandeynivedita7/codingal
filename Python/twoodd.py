def TwoOdd(arr, size):
  xorof2 = arr[0]
  x = 0
  y = 0
  SetBit = 0
  for i in range(1,size):

    xorof2 = xorof2 ^ arr[i]#Because numbers that occur an even number of times cancel (a ^ a = 0), the final xorof2 equals A ^ B, where A and B are the two distinct numbers that occur odd times.
  SetBit = xorof2 & ~(xorof2-1)
  for i in range(size):
    if(arr[i]& SetBit):
      x = x ^ arr[i]
    else:
      y = y ^ arr[i]

  print("TwoOdd elements are",x,"&",y)

arr = []
arr_size = int(input("Enter the size of the array"))
for i in range(0,arr_size):
  z = int(input("Enter element"))
  arr.append(z)

print("TwoOdd")
#1011 reverse 1101
#2 10 reverse 01 1 decimal