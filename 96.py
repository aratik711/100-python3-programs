"""

Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array.
Input:
2
Output:
['#FD41D2', '#D804EC']

"""
import random
num = int(input())
r = lambda: random.sample(range(0,256), num)
colors = ['#%02X%02X%02X' % (c,c,c) for c in list(r())]
print (colors)
