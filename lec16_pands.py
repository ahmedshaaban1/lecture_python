# http://www.python-course.eu/pandas.php
import pandas as pd
import numpy as np
import sys as ss

#######  series 

## 1
S = pd.Series([11, 28, 72, 3, 5, 8])

print(S.index)
print(S.values)

##  2
fruits = ['apples', 'oranges', 'cherries', 'pears']
quantities = [20, 33, 52, 10]
S = pd.Series(quantities, index=fruits)
S
print(S['apples'])
print((S + 3) * 4)
print("======================")
np.sin(S)

##  3
cities = {"London":   8615246, 
          "Berlin":   3562166, 
          "Madrid":   3165235, 
          "Rome":     2874038, 
          "Paris":    2273305, 
          "Vienna":   1805681, 
          "Bucharest":1803425, 
          "Hamburg":  1760433,
          "Budapest": 1754000,
          "Warsaw":   1740119,
          "Barcelona":1602386,
          "Munich":   1493900,
          "Milan":    1350680}
          
pd.Series(cities,["London"])

city_series = pd.Series(cities)
print(city_series)
my_cities = ["London", "Paris", "Zurich", "Berlin", 
             "Stuttgart", "Hamburg"]
my_city_series = pd.Series(cities, index=my_cities)
print(my_city_series)
print(my_city_series.isnull())

########## DataFrame

cities = {"name": ["London", "Berlin", "Madrid", "Rome", 
                   "Paris", "Vienna", "Bucharest", "Hamburg", 
                   "Budapest", "Warsaw", "Barcelona", 
                   "Munich", "Milan"],
          "population": [8615246, 3562166, 3165235, 2874038,
                         2273305, 1805681, 1803425, 1760433,
                         1754000, 1740119, 1602386, 1493900,
                         1350680],
          "country": ["England", "Germany", "Spain", "Italy",
                      "France", "Austria", "Romania", 
                      "Germany", "Hungary", "Poland", "Spain",
                      "Germany", "Italy"]}
city_frame = pd.DataFrame(cities)
print(city_frame)

# adding another column
ordinals = ["first", "second", "third", "fourth",
            "fifth", "sixth", "seventh", "eigth",
            "ninth", "tenth", "eleventh", "twelvth",
            "thirteenth"]
city_frame = pd.DataFrame(cities, index=ordinals)
print(city_frame)

# printing with rearranging columns orders
city_frame = pd.DataFrame(cities,
                          columns=["name", 
                                   "country", 
                                   "population"],
                          index=ordinals)
print(city_frame)
city_frame.sum()
city_frame["population"].sum()

city_frame = pd.DataFrame(cities,
                          columns=["name", 
                                   "country", 
                                   "area",
                                   "population"],
                          index=ordinals)
print(city_frame)
city_frame["area"] = 1572
print(city_frame)

# area in square km:
area = [1572, 891.85, 605.77, 1285, 
        105.4, 414.6, 228, 755, 
        525.2, 517, 101.9, 310.4, 
        181.8]
city_frame["area"] = area
print(city_frame)

city_frame = city_frame.sort(columns="area", ascending=False)
print(city_frame)
