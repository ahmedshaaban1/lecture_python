#http://www.python-course.eu/numpy_reading_writing.php
import numpy as np

# saving text files
x = np.array([[1, 2, 3], 
              [4, 5, 6],
              [7, 8, 9]], np.int32)
np.savetxt("io/test.txt", x)
np.savetxt("io/test2.txt", x, fmt="%2.3f", delimiter=",")
np.savetxt("io/test3.txt", x, fmt="%04d", delimiter=" :-) ")

# loading text files.
y = np.loadtxt("io/test.txt")
y = np.loadtxt("io/test2.txt", delimiter=",")
y = np.loadtxt("io/test3.txt", delimiter=" :-) ")
y = np.loadtxt("io/test3.txt", delimiter=" :-) ", usecols=(0,2))

# npy files (binary platform independent like .mat files)
x = np.arange(10)
np.save("outf", x)
np.load('outf.npy')