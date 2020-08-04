"""

Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

"""
class Circle(object):
    def __init__(self, radius = 0):
        self.radius = radius
    def area(self):
        return self.radius**2*3.14

circle = Circle(5)
print(circle.area())