"""

Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.

"""
def square():
    sq = dict()
    for num in range(1,21):
        sq[num] = num**2
    print(','.join([str(sq[x]) for x in sq]))

square()