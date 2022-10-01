#  numpy tut 1
import numpy as np
## 1-D array
myarr = np.array([1,5,787])
print(myarr)
l = [5,15,9,6,7]
myarry = np.array(l) # converting the list into array
print(myarry)
myarr2 = np.array([1,5,787],np.int16) # 16 bits # passing the size of array element
print(myarr2)
# accessing the element of the array
print(myarry[2])
print(myarry.shape) # getting size of array
print(myarr.dtype) # getting type of array element
print(myarr2.dtype) # getting type of array element
# changing the element of array
myarr[1] = 151
print(myarr)