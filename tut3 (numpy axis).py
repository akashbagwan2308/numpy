# Numpy Axis
#   1-D array -------- 1 axis , [Axis 0]
#   2-D array -------- 2 axis , [Axis 0, Axis 1]
import numpy as np

x = [[1,2,3],[4,5,6],[7,1,0]]
ar = np.array(x)
print('ar :\n',ar)
# [[1 2 3]     axis 0 = ie column wise
#  [4 5 6]     axis 1 = ie row wise
#  [7 1 0]]
print("Sum : ",ar.sum(axis=0))  # sum along axis 0
print("Sum : ",ar.sum(axis=1))  # sum along axis 1
T = ar.T
print("Transpose :\n",T)
print("Sum : ",T.sum(axis=0))  # sum along axis 0
print("Sum : ",T.sum(axis=1))  # sum along axis 1
f = ar.flat
for item in f:
    print(item)   # will print all the element of array
print("No of dimension :",ar.ndim)
print("Size :",ar.size)
print("Total no of bytes :",ar.nbytes )
# ----------------------------------------------------------------------------
one = np.array([1,55,785,45,95,56])
print(one.argmax())   # gives the index of maximum value element
print(one.argmin())   # gives the index of minimum value element
print(one.argsort()) # gives index or sorted array

arr = np.array(x)
print("Max: ",arr.argmax())   # gives the index of maximum value element
print("Max in axis 0: ",arr.argmax(axis=0))   # gives the index of maximum value element in axis 0
print("Max in axis 1: ",arr.argmax(axis=1))   # gives the index of maximum value element in axis 1
print("Min: ",arr.argmin())   # gives the index of minimum value element
print("Min in axis 0: ",arr.argmin(axis=0))   # gives the index of minimum value element in axis 0
print("Min in axis 1: ",arr.argmin(axis=1))   # gives the index of minimum value element in axis 1