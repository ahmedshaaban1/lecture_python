import numpy as np

# http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.linalg.solve.html
# Solve the equation a x = b for x.
# Solve the system of equations 3 * x0 + x1 = 9 and x0 + 2 * x1 = 8:

a = np.array([[3,1], [1,2]])
b = np.array([9,8])
x = np.linalg.solve(a, b)
x
np.dot(a, x)
