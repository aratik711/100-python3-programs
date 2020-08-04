"""

Write a function to compute 5/0 and use try/except to catch the exceptions.

"""
def throws():
    return 5/0

try:
    throws()
except ZeroDivisionError:
    print("Division by zero!")
except Exception as ex:
    print ("Caught an exception")
finally:
    print ("Finally block")