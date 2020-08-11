"""

Please generate a random float where the value is between 10 and 100 using Python math module.

Hints: Use random.random() to generate a random float in [0,1].

"""
import random
min = 10
max = 100
rand_num = (max-min)*random.random() + min
print (rand_num)
print (random.uniform(10,100))