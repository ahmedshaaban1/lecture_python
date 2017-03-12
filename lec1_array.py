#http://www.python-course.eu/numpy.php
import numpy as np
# one dimension
a=np.array([1,2,3])
a.ndim
np.ndim(a)
a.shape
a[:,np.newaxis]# this method is only for one dimension array, otherwise use Transpose.
a[:,np.newaxis].shape

# two dimension row & column
b=np.array([[1,2,3,4]])
b.ndim
b.shape
b.T
np.transpose(b)

c=np.array([[1],[2],[3]])
c.ndim
c.shape 
np.transpose(c)

# how to wirte array of rows and columns
d=np.array([[1,2,3],[4,5,6]])
# indexing
print(d[0,0])
print(d[1,:])
     
f=np.array([1,2,3,4,5,6,7,8,9,10])
print(f[::2])
print(f[::-1])
print(f[3::2])  

# ideantity and zeros and ones

print(np.ones([3,2]))
print(np.zeros([3,2]))  

  