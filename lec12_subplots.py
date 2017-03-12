import numpy as np
import matplotlib.pyplot as plt
from numpy import e, pi, sin, exp, cos

python_course_green = "#476042"
plt.figure(figsize=(6, 4))
plt.xticks(())
plt.yticks(())
plt.subplot(221) # equivalent to: plt.subplot(2, 2, 1)
plt.text(0.5, # x coordinate, 0 leftmost positioned, 1 rightmost
         0.5, # y coordinate, 0 topmost positioned, 1 bottommost
         'subplot(2,2,1)', # the text which will be printed
         horizontalalignment='center', # shortcut 'ha' 
         verticalalignment='center', # shortcut 'va'
         fontsize=20, # can be named 'font' as well
         alpha=.5 # float (0.0 transparent through 1.0 opaque)
         )
plt.subplot(224, axisbg=python_course_green)
plt.text(0.5, 0.5, 
         'subplot(2,2,4)', 
         ha='center', va='center',
         fontsize=20, 
         color="y")
         
# again but using add_subplot method
python_course_green = "#476042"
fig = plt.figure(figsize=(6, 4))
sub1 = fig.add_subplot(221) # equivalent to: plt.subplot(2, 2, 1)
sub1.set_xticks([]) 
sub1.set_yticks([]) 
sub1.text(0.5, # x coordinate, 0 leftmost positioned, 1 rightmost
          0.5, # y coordinate, 0 topmost positioned, 1 bottommost
          'subplot(2,2,1)', # the text which will be printed
          horizontalalignment='center', # shortcut 'ha' 
          verticalalignment='center', # shortcut 'va'
          fontsize=20, # can be named 'font' as well
          alpha=.5 # float (0.0 transparent through 1.0 opaque)
          )
sub2 = fig.add_subplot(224, axisbg=python_course_green)
sub2.set_xticks([])
sub1.set_yticks([]) 
sub2.text(0.5, 0.5, 
          'subplot(2,2,4)', 
          ha='center', va='center',
          fontsize=20, 
          color="y") 
          
# four panels
fig = plt.figure(figsize=(6, 4))
sub1 = plt.subplot(2, 2, 1)
sub1.set_xticks(())
sub1.set_yticks(())
sub1.text(0.5, 0.5, 'subplot(2,2,1)', ha='center', va='center',
        size=20, alpha=.5)
sub2 = plt.subplot(2, 2, 2)
sub2.set_xticks(())
sub2.set_yticks(())
sub2.text(0.5, 0.5, 'subplot(2,2,2)', ha='center', va='center',
        size=20, alpha=.5)
sub3 = plt.subplot(2, 2, 3)
sub3.set_xticks(())
sub3.set_yticks(())
sub3.text(0.5, 0.5, 'subplot(2,2,3)', ha='center', va='center',
        size=20, alpha=.5)
sub4 = plt.subplot(2, 2, 4, axisbg=python_course_green)
sub4.set_xticks(())
sub4.set_yticks(())
sub4.text(0.5, 0.5, 'subplot(2,2,4)', ha='center', va='center',
        size=20, alpha=.5, color="y")
fig.tight_layout()
plt.show()   

 # real examples with real plots
def f(t):
    return exp(-t) * cos(2*pi*t)
def fp(t):
    return -2*pi * exp(-t) * sin(2*pi*t) - e**(-t)*cos(2*pi*t)
def g(t):
    return sin(t) * cos(1/(t+0.1))
def g(t):
    return sin(t) * cos(1/(t))
python_course_green = "#476042"
fig = plt.figure(figsize=(6, 4))
t = np.arange(-5.0, 1.0, 0.1)
sub1 = fig.add_subplot(221) # instead of plt.subplot(2, 2, 1)
sub1.set_title('The function f') # non OOP: plt.title('The function f')
sub1.plot(t, f(t))
sub2 = fig.add_subplot(222, axisbg="lightgrey")
sub2.set_title('fp, the derivation of f')
sub2.plot(t, fp(t))
t = np.arange(-3.0, 2.0, 0.02)
sub3 = fig.add_subplot(223)
sub3.set_title('The function g')
sub3.plot(t, g(t))
t = np.arange(-0.2, 0.2, 0.001)
sub4 = fig.add_subplot(224, axisbg="lightgrey")
sub4.set_title('A closer look at g')
sub4.set_xticks([-0.2, -0.1, 0, 0.1, 0.2])
sub4.set_yticks([-0.15, -0.1, 0, 0.1, 0.15])
sub4.plot(t, g(t))
plt.plot(t, g(t))
plt.tight_layout()
plt.show()     


# example for subplots design.
X = [ (2,1,1), (2,3,4), (2,3,5), (2,3,6) ]
for nrows, ncols, plot_number in X:
    plt.subplot(nrows, ncols, plot_number)
plt.show()    
# another example for subplot design.
X = [ (1,2,1), (3,2,2), (3,2,4), (3,2,6) ]
for nrows, ncols, plot_number in X:
    plt.subplot(nrows, ncols, plot_number)
    plt.xticks([])
    plt.yticks([])
                                                                   
plt.show()    

# a plot inside a plot
fig = plt.figure()
X = [1, 2, 3, 4, 5, 6, 7]
Y = [1, 3, 4, 2, 5, 8, 6]
axes1 = fig.add_axes([0.1, 0.1, 0.9, 0.9]) # main axes
axes2 = fig.add_axes([0.2, 0.6, 0.4, 0.3]) # inset axes
# main figure
axes1.plot(X, Y, 'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('title')
# insert
axes2.plot(Y, X, 'g')
axes2.set_xlabel('y')
axes2.set_ylabel('x')
axes2.set_title('title inside');     

# axes types
fig, axes = plt.subplots(1, 3, figsize=(10, 4))
x = np.arange(0, 5, 0.25)
axes[0].plot(x, x**2, x, x**3)
axes[0].set_title("default axes ranges")
axes[1].plot(x, x**2, x, x**3)
axes[1].axis('tight')
axes[1].set_title("tight axes")
axes[2].plot(x, x**2, x, x**3)
axes[2].set_ylim([0, 60])
axes[2].set_xlim([2, 5])
axes[2].set_title("custom axes range");

# lograrthmic scale
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x = np.arange(0, 5, 0.25)
ax.plot(x, x**2, x, x**3)
ax.set_yscale("log")
plt.show()

# twin axes
fig, ax1 = plt.subplots()
x = np.arange(1,7,0.1)
ax1.plot(x, 2 * np.pi * x, lw=2, color="blue")
ax1.set_ylabel(r"Circumference $(cm)$", fontsize=16, color="blue")
for label in ax1.get_yticklabels():
    label.set_color("blue")
    
ax2 = ax1.twinx()
ax2.plot(x, np.pi * x ** 2, lw=2, color="darkgreen")
ax2.set_ylabel(r"area $(cm^2)$", fontsize=16, color="darkgreen")
for label in ax2.get_yticklabels():
    label.set_color("darkgreen")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                