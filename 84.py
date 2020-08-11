"""

Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

"""
class Person(object):
    def getGender(self):
        return "Apache helicopter"

class Female(Person):
    def getGender(self):
        return "Female"

class Male(Person):
    def getGender(self):
        return "Male"

aMale = Male()
aFemale = Female()
print(aMale.getGender())
print(aFemale.getGender())