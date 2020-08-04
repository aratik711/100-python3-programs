"""

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

"""
def square():
    sq = []
    for num in range(1,21):
        sq.append(num**2)
    print(*sq[-5:],sep=',')

square()