"""

Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

"""
class Rectangle(object):
    def __init__(self, l=0, b=0):
        self.l = l
        self.b = b

    def area(self):
        return self.l*self.b

rectangle = Rectangle(3,4)
print(rectangle.area())