"""

Please write a program which prints all permutations of [1,2,3]

Hints: Use itertools.permutations() to get permutations of list.

"""
import itertools
li = [1,2,3]
print(list(itertools.permutations(li)))