"""

Given a name, return a string with the message:

One for X, one for me.
Where X is the given name.

However, if the name is missing, return the string:

One for you, one for me.

"""
name = input()
if len(name)==0:
    name = "you"
print("One for "+ name +", one for me.")
