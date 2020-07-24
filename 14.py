"""

Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. Suppose the following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9

"""
line = input()
count = {'U': 0, 'L': 0}
for char in line:
    if char.isupper():
        count['U'] += 1
    if char.islower():
        count['L'] += 1

print("UPPER CASE " + str(count['U']) +" LOWER CASE " + str(count['L']))