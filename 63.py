"""

The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0 f(n)=1 if n=1 f(n)=f(n-1)+f(n-2) if n>1

Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.

Example: If the following n is given as input to the program:

7

Then, the output of the program should be:

0,1,1,2,3,5,8,13

"""
def fib(num):
    if (num==0) or (num==1):
        return num
    else:
        return fib(num-1) + fib(num-2)

num = int(input())
fib_list = [str(fib(x)) for x in range(0, num+1)]
print (','.join(fib_list))