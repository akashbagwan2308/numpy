# Array creation methods:
import numpy as np

l = [1,5,89,6]
myarr = np.array(l)
print(myarr)
# 2-D array
listarray = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(listarray)
print(listarray.dtype) # it give size of element
print(listarray.size)  # it gives total no of array
print(listarray.shape) # it gives order of array
# zero array
zeros = np.zeros((2,5))
print(zeros)
# ones array
ones = np.ones((2,5))
print(ones)
# array in range
range = np.arange(15) # upto 14
print(range)
reg = np.arange(2,15) # from 2 to 14
print(reg)
reg2 = np.arange(2,10,0.8) # from 2 to 10 , elements having diff of 0.8
print(reg2)
# aray using linspace
lspace = np.linspace(2,10,6)  # from 2 to 10 ,will give 6 elements of equal interval
print(lspace)
emp = np.empty((2,3)) # it gives empty array of random values
print(emp)
emplike = np.empty_like(lspace)
print(emplike)
# identy array
# eye = np.eye(3)  # identity array of 3 rows 3 column
eye = np.identity(3)  # identity array of 3 rows 3 column
print(eye)
eye2 = np.eye(3,5)  # identity array of 3 rows 5 column
print(eye2)
# diagonal array
dia = np.diag([1,2,3])
print(dia)
# reshaping array
a = np.arange(99)
r = a.reshape(3,33)
print(r)
g = r.ravel()
print(g)
