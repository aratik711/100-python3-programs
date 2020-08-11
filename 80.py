"""

By using list comprehension, please write a program generate a 3x5x8 3D array whose each element is 0.

Hints: Use list comprehension to make an array.

"""
arr = [[ [0 for col2 in range(9)] for col1 in range(6)] for row in range(4)]
print (arr)