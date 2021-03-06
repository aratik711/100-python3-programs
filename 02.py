"""

Question: Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

"""

def fact(num):
    if (num == 0) or (num == 1):
        return num
    return(num*fact(num-1))

num = int(input())
print(fact(num))