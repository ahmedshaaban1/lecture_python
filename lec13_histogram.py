# http://www.python-course.eu/matplotlib_histograms.php
import matplotlib.pyplot as plt
import numpy as np

gaussian_numbers = np.random.normal(size=10000)
plt.hist(gaussian_numbers)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

n, bins, patches = plt.hist(gaussian_numbers)
print("n: ", n, sum(n))
print("bins: ", bins)
for i in range(len(bins)-1):
    print(bins[i+1] -bins[i])
print("patches: ", patches)
print(patches[1])

plt.figure()
plt.hist(gaussian_numbers, bins=100)
plt.show()

# normalized histogram 
plt.figure()
plt.hist(gaussian_numbers, bins=100, normed=True)
plt.show()
# normalized histogram and set the sum to 1
plt.figure()
plt.hist(gaussian_numbers, 
         bins=100, 
         normed=True, 
         stacked=True, 
         edgecolor="#6A9662",
         color="#DDFFDD")
plt.show()

# cumilative histogram
plt.figure()
plt.hist(gaussian_numbers, 
         bins=100, 
         normed=True,
         stacked=True,
         cumulative=True)
plt.show()

# bar plots
plt.figure()
bars = plt.bar([1,2,3,4], [1,4,9,16])
bars[0].set_color('green')
plt.show()
