## this script should be exectuted several times to see how it works.
import matplotlib.pyplot as plt
## Generating random number.
import numpy as np
print(np.random.randint(1, 7))
print(np.random.randint(1, 7, size=1))
print(np.random.randint(1, 7, size=10))
print(np.random.randint(1, 7, size=(5, 4)))

## random choises
from random import choice
print(choice("abcdefghij"))
print(choice(["scientist", "philosopher", "engineer", "priest"]))
print(choice(("apples", "bananas", "cherries")))

##  find intervals
def find_interval(x, partition):
    """ find_interval -> i
        "i" will be the index for which applies
        partition[i] < x < partition[i+1], if such an index exists.
        -1 otherwise
        """
    
    for i in range(0, len(partition)):
        print i
        if x < partition[i]:
            return i-1
    return -1
    
find_interval(9,[10,20,30,40,50])
find_interval(10,[10,20,30,40,50])
find_interval(20,[10,20,30,40,50])
print("dfdfdfdfd") 

###  Random Seed.
# a number used to initialize a pseudorandom number generator.
# Yet, the seed matters in terms of security. 
# If you know the seed, you could for example generate the secret encryption key which is based on this seed.

np.random.seed(42)
for _ in range(10): #generally use '_' to denote values I don't care about 
     print(np.random.randint(1, 10))
    
print("\nLet's create the same random numbers again:")
np.random.seed(42)
for _ in range(10):
     print(np.random.randint(1, 10))

## 

def random_ones_and_zeros(p):
    """ p: probability 0 <= p <= 1
        returns a 1 with the probability p
    """
    x = np.random.random() # this return random number between 0 and 1.
    if x < p:
        return 1
    else:
        return 0
     
n = 1000000     
aa=np.zeros(n)           
for i in range(n):
      aa[i]=random_ones_and_zeros(0.8)
               
plt.hist(aa)               


#Synthetical Sales Figures
fh = open("sales_figures.csv", "w")
fh.write("Year, Frankfurt, Munich, Berlin, Zurich, Hamburg, London, Toronto, Strasbourg, Luxembourg, Amsterdam, Rotterdam, The Hague\n")
sales = np.array([1245.89, 2220.00, 1635.77, 1936.25, 1002.03, 2099.13,  723.99, 990.37, 541.44, 1765.00, 1802.84, 1999.00])
for year in range(1997, 2016):
    line = str(year) + ", " + ", ".join(map(str, sales))
    fh.write(line + "\n")
    if year % 4 == 0:
         min_percent = 0.98  # corresponds to -1.5 %
         max_percent = 1.06   # 6 %
         growthrates = (max_percent - min_percent) * np.random.random_sample(12) + min_percent
         #growthrates = 1 + (np.random.rand(12) * max_percent - negative_max) / 100
         sales = np.around(sales*growthrates, 2)
fh.close()

## exercies
# Let's do some more die rolling. Prove empirically - by writing a simulation program - 
# that the probability for the combined events "
# an even number is rolled" (E) and "A number greater than 2 is rolled" is 1/3.

outcomes = [ np.random.randint(1, 6) for _ in range(10000)]
even_pips = [ x for x in outcomes if x % 2 == 0]
greater_two = [ x for x in outcomes if x > 2]
combined = [ x for x in outcomes if x % 2 == 0 and x > 2]
print(len(even_pips) / len(outcomes))
print(len(greater_two) / len(outcomes))
print(len(combined) / len(outcomes))
