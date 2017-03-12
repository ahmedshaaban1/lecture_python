# http://www.python-course.eu/matplotlib_legends_and_annotations.php
# legends and annotations
import numpy as np
import matplotlib.pyplot as plt

# simple example.
ax = plt.gca()
ax.plot([1, 2, 3, 4])
ax.legend(['A simple line'])

# two labels
x = np.linspace(0, 25, 1000)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, '-b', label='sine')
plt.plot(x, y2, '-r', label='cosine')
plt.legend(loc='upper left')
plt.ylim(-1.5, 2.0)
plt.show()

# two labels Latex
X = np.linspace(0, 25, 1000)
F1 = np.sin(0.5 * X)
F2 = 3 * np.cos(0.8*X)
plt.plot(X, F1, label="$sin(0.5 * x)$")
plt.plot(X, F2, label="$3 sin(x)$")
plt.legend(loc='upper right')
plt.show()
# two labels Latex different position
X = np.linspace(0, 25, 1000)
F1 = np.sin(0.5 * X)
F2 = 3 * np.cos(0.8*X)
plt.plot(X, F1, label="$sin(0.5 * x)$")
plt.plot(X, F2, label="$3 sin(x)$")
plt.legend(loc='best')
plt.show()
# again for best position 
X = np.linspace(-2 * np.pi, 2 * np.pi, 70, endpoint=True)
F1 = np.sin(0.5*X)
F2 = -3 * np.cos(0.8*X)
plt.xticks( [-6.28, -3.14, 3.14, 6.28],
        [r'$-2\pi$', r'$-\pi$', r'$+\pi$', r'$+2\pi$'])
plt.yticks([-3, -1, 0, +1, 3])
plt.plot(X, F1, label="$sin(0.5x)$")
plt.plot(X, F2, label="$-3 cos(0.8x)$")
plt.legend(loc='best')
plt.show()

# annotate
X = np.linspace(-2 * np.pi, 3 * np.pi, 70, endpoint=True)
F1 = np.sin(X)
F2 = 3 * np.sin(X)
ax = plt.gca()
plt.xticks( [-6.28, -3.14, 3.14, 6.28],
        [r'$-2\pi$', r'$-\pi$', r'$+\pi$', r'$+2\pi$'])
plt.yticks([-3, -1, 0, +1, 3])
x = 3 * np.pi / 4
plt.scatter([x,],[3 * np.sin(x),], 50, color ='blue')
plt.annotate(r'$(3\sin(\frac{3\pi}{4}),\frac{3}{\sqrt{2}})$',
         xy=(x, 3 * np.sin(x)), 
         xycoords='data',
         xytext=(+20, +20), 
         textcoords='offset points', 
         fontsize=16,
         arrowprops=dict(facecolor='blue'))
plt.plot(X, F1, label="$sin(x)$")
plt.plot(X, F2, label="$3 sin(x)$")
plt.legend(loc='lower left')
plt.show()

