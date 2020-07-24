"""

Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a. Suppose the following input is supplied to the program: 9 Then, the output should be: 11106

"""
a = input()
num1 = int("%s" % a)
num2 = int("%s%s" % (a, a))
num3 = int("%s%s%s" % (a, a, a))
num4 = int("%s%s%s%s" % (a, a, a, a))
print(str(num1+num2+num3+num4))