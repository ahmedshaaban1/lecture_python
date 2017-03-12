#http://www.python-course.eu/matplotlib_spines_and_ticks.php

import numpy as np
import matplotlib.pyplot as plt
import sys as ss
# Moving the Border Lines and Polishing up the Axes Notations

X = np.linspace(-2 * np.pi, 2 * np.pi, 70, endpoint=True)
F1 = np.sin(2* X)
F2 = (2*X**5 + 4*X**4 - 4.8*X**3 + 1.2*X**2 + X + 1)*np.exp(-X**2)
# get the current axes, creating them if necessary:
ax = plt.gca()
# moving bottom spine up to y=0 position:
#ax.xaxis.set_ticks_position('bottom')
#ax.spines['bottom'].set_position(('data',0))
# moving left spine to the right to position x == 0:
#ax.yaxis.set_ticks_position('right')
#ax.spines['right'].set_position(('data',0))

# making the top and right spine invisible:
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)

ax.xaxis.set_ticks_position('top')
ax.spines['top'].set_color('red')
ax.spines['top'].set_position(('axes',0.5)) # zero , center, ('axes',0.6)
# note the number ('axes', 0.8) means 0.8 percentage of the axes length
# thus there is no number here above 1 

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_color('red')
ax.spines['left'].set_position(('axes',0.5)) # zero , center, ('axes',0.6)

plt.plot(X, F1)
plt.plot(X, F2)
plt.show()

ss.exit()
# Setting Tick Labels
X = np.linspace(-2 * np.pi, 2 * np.pi, 70, endpoint=True)
F1 = X * np.sin(X)
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
# labelling the X ticks:
plt.xticks( [-6.28, -3.14, 3.14, 6.28],
        [r'$-2\pi$', r'$-\pi$', r'$+\pi$', r'$+2\pi$'])
plt.yticks([-3, -1, 0, +1, 3])
plt.plot(X, F1)
plt.show()

# adjusting the ticklabel 
X = np.linspace(-2 * np.pi, 2 * np.pi, 170, endpoint=True)
F1 = np.sin(X**3 / 2)
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.xticks( [-6.28, -3.14, 3.14, 6.28],
        [r'$-2\pi$', r'$-\pi$', r'$+\pi$', r'$+2\pi$'])
plt.yticks([-3, -1, 0, +1, 3])
for xtick in ax.get_xticklabels():
    xtick.set_fontsize(18)
    xtick.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7 ))
for ytick in ax.get_yticklabels():
    ytick.set_fontsize(14)
    ytick.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7 ))
    
plt.plot(X, F1, label="$sin(x)$")
plt.legend(loc='lower left')
plt.show()
