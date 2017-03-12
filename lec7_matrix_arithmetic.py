#http://www.python-course.eu/matrix_arithmetic.php
import numpy as np
import sys as ss

x = np.array([1,5,2])
y = np.array([7,4,1])
print(x + y)
print(x * y)
print(x - y)
print(x / y)
print(x % y)
# dot products
dot=np.dot(x,y)
print(dot)
# finding the anlge between two vectors based on the dot products.
x_modulus = np.sqrt((x*x).sum())
y_modulus = np.sqrt((y*y).sum())
cos_angle = dot / x_modulus / y_modulus # cosine of angle between x and y
angle = np.arccos(cos_angle)
angle * 360 / 2 / np.pi # angle in degrees
# cross products.
print(np.cross(x,y))
print(np.cross(y,x))


# matrix operations
x = np.array( ((2,3), (3, 5)) )
y = np.array( ((1,2), (5, -1)) )
print("dfdfdfd")
print(x * y)  # this is element wise multiplication as we have array
x = np.matrix( ((2,3), (3, 5)) )
y = np.matrix( ((1,2), (5, -1)) )
print(x*y) # this is matrix multiplication 
print(np.dot(x,y)) # this is the same as the preceeding equation.