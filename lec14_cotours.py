# http://www.python-course.eu/matplotlib_contour_plot.php

# generating meshgrid
import numpy as np
import matplotlib.pyplot as plt

xlist = np.linspace(-2.0, 2.0,5)
ylist = np.linspace(-1.0, 1.0,3)
X, Y = np.meshgrid(xlist, ylist)
print(xlist)
print(ylist)
print(X)
print(Y)

Z = np.sqrt(X**2 + Y**2) # we donot have here loop as we used meshgrid.

plt.figure()
cp = plt.contour(X, Y, Z)
plt.clabel(cp, inline=True, 
          fontsize=10)
plt.title('Contour Plot')
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.show()

# dashed black countours 
plt.figure()
cp = plt.contour(X, Y, Z, colors='black', linestyles='dashed')
plt.clabel(cp, inline=True, 
          fontsize=10)
plt.title('Contour Plot')
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.show()

# Filled contours
cp = plt.contourf(X, Y, Z)
plt.colorbar(cp)
plt.title('Filled Contours Plot')
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.show()

# controlling the levels of contours
xlist = np.linspace(-3.0, 3.0, 100)
ylist = np.linspace(-3.0, 3.0, 100)
X, Y = np.meshgrid(xlist, ylist)
Z = np.sqrt(X ** 2 + Y ** 2 )
plt.figure()
levels = [0.0, 0.2, 0.5, 0.9, 1.5, 2.5, 3.5]
contour = plt.contour(X, Y, Z, levels, colors='k')
plt.clabel(contour, colors = 'k', fmt = '%2.1f', fontsize=12)
contour_filled = plt.contourf(X, Y, Z, levels)
plt.colorbar(contour_filled)
plt.title('Plot from level list')
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.show()

# Heart
y, x = np.ogrid[-1:2:100j, -1:1:100j]
plt.contour(x.ravel(), 
            y.ravel(), 
            x**2 + (y-((x**2)**(1.0/3)))**2, 
            [1],
            colors='red',)
plt.axis('equal')
plt.show()