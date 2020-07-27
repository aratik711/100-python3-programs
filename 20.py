"""

Define a a generator function which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

"""
def divSeven(n):
    i = 0
    while i<n:
        i=i+1
        if i%7==0:
            yield i

for num in divSeven(100):
    print(num)