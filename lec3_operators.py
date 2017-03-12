#http://www.python-course.eu/numpy_numerical_operations_on_numpy_arrays.php
import numpy as np

# list is different from array. 
# List understand the addition, multiplication,.. in different ways.
lst = [1,2,3,4,5,6,7,8,9,10]
#print(lst+2) # ==> this will give you error

res = []
for val in lst:
    res.append(val + 2)
print(res)

print(lst*2)

# array is totally different from list.
v = np.array(lst)
print(v + 2)
print(v*2)
print(v**2)

# Matrixes addition& muliplications

A= np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])
             
B= np.ones([3,3])

print(A+B)
print(A*B)
print(np.dot(A,B))

print(A[1,:]*B[1,:])
print(np.dot(A[1,:],B[1,:]))

# amazing trick to not use dot. 
# convert array into matrix 
AA=np.mat(A)
BB=np.mat(B)
print(AA*BB)
print(A*B)


# array comparisons
A == B
print(np.array_equal(A,B))
print(np.array_equal(A,A))

# array broadcasting.
A = np.array([ [11, 12, 13], [21, 22, 23], [31, 32, 33] ])
B = np.array([1, 2, 3])

print("Multiplication with broadcasting: ")
print(A * B)
print("... and now addition with broadcasting: ")
print(A + B)
 
 
# distance matrixes
cities = ["Barcelona", "Berlin", "Brussels", "Bucharest",
          "Budapest", "Copenhagen", "Dublin", "Hamburg", "Istanbul",
          "Kiev", "London", "Madrid", "Milan", "Moscow", "Munich",
          "Paris", "Prague", "Rome", "Saint Petersburg", 
          "Stockholm", "Vienna", "Warsaw"]
dist2barcelona = [0,  1498, 1063, 1968, 
                  1498, 1758, 1469, 1472, 2230, 
                  2391, 1138, 505, 725, 3007, 1055, 
                  833, 1354, 857, 2813, 
                  2277, 1347, 1862]
dists =  np.array(dist2barcelona[:12])
print(dists)
print(np.abs(dists - dists[:, np.newaxis]))
# what habben here is that boradcasting occurs for both dist and dists[:,np.newaxis]
# for example
b=np.array([1,2,3])
print(b-b[:,np.newaxis])
