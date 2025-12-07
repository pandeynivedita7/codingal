import numpy as np# n dim array
arr=np.array([1,2,3,4,5])# 1d array
print(arr)
print(type(arr))# <class 'numpy.ndarray'> what is type specific the datatype of array
#a=10 print(type(a)) # <class 'int'> datatype of integer
print(arr[3])#4 accessing element at index 3
print(arr[0:4])#[1 2 3 4] slicing array from index 0 to 3
print(arr.dtype)#int32 datatype of array elements
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])#  array
print(arr1)
print(arr1.shape)#(3, 3) shape of array rows and columns
#arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])#  array 2 dim
#3 dim array
arr3=np.array([[[1,2,3,4],[4,5,6,5],[7,8,9,7]],
               [[10,11,12,4],[13,14,15,7],[16,17,18,9]],
               [[19,20,21,5],[22,23,24,7],[25,26,27,0]]])
print(arr3.shape)

arr