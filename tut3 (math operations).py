# matrix operations
import numpy as np

x = [[1,2,3],[4,5,6],[7,1,0]]
ar = np.array(x)
y=  [[2,7,8],[2,8,4],[1,0,8]]
ar2 = np.array(y)
print("Sum :\n", ar+ar2)
print("Product :\n", ar*ar2)
print("Square root :\n",np.sqrt(ar))
print("Square :\n",np.square(ar))
print(np.where(ar>5))
print(np.count_nonzero(ar))

