#http://www.python-course.eu/numpy_changing_dimensions.php
import numpy as np

## ===>>> array flatening.
A = np.array( [[ 0,  10],
               [ 20,  30],
               [ 40,  50],
               [ 60,  70]])
Flattened_X = A.flatten()
Flattened_X.shape
print(Flattened_X)
print(A.flatten(order="C"))
print(A.flatten(order="F"))
print(A.flatten(order="A"))
## ======>>>>> Reshaping.
print(" Here is the reshape function")
Y= A.reshape((2,4))
print(Y)

x = np.array([[11,22],
             [33,44]])
y = np.array([[6,7],
              [8,9]])
## =====>>>> array concatentation.
c = np.concatenate((x,y),axis=0)
print(c)
c = np.concatenate((x,y),axis=1)
print(c)

##=====>>>> adding new dimension.
x = np.array([2,5,18,14,4])
y = x[:, np.newaxis]
print(y)

## =====>>>> tile up array.
x = np.array([ 3.4])
print(np.tile(x, (5,))) 

x = np.array([ [1, 2], [3, 4]])
print(np.tile(x, (3,4)))
