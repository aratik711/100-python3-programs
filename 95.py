"""

Determine if a word or phrase is an isogram.

An isogram (also known as a "nonpattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.

Examples of isograms:

lumberjacks
background
downstream
six-year-old
The word isograms, however, is not an isogram, because the s repeats.

"""
str = input()
isIsogram = False
str = str.lower().replace(' ', '').replace('-','')
if (len(str) == len(set(str))):
    isIsogram = True

if isIsogram:
    print("%s is Isogram" % str)
else:
    print("%s is not Isogram" % str)