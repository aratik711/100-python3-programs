"""

Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).

"""
def square():
    sq = []
    for num in range(1,21):
        sq.append(num**2)
    print(tuple(sq))

square()