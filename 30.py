"""

Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

"""
def square(num):
    sq = dict()
    for num in range(1,num+1):
        sq[num] = num**2

    print(sq)

square(20)