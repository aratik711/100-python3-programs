"""

Define a class, which have a class parameter and have a same instance parameter.

"""
class Person:

    name = "Person"

    def __init__(self, name=None):
        self.name = name

john = Person("John")
print("%s name is %s" % (Person.name, john.name))

jane = Person()
jane.name = "Jane"
print("%s name is %s" % (Person.name, jane.name))