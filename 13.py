"""

Write a program that accepts a sentence and calculate the number of letters and digits. Suppose the following input is supplied to the program: hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3

"""
line = input()
count = {'ALPHA': 0, 'NUM': 0}
for char in line:
    if(char.isalpha()):
        count['ALPHA'] += 1
    if char.isdigit():
        count['NUM'] += 1

print("LETTERS", count["ALPHA"])
print("DIGITS", count["NUM"])