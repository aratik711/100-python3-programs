"""

Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.

"""
answer = []
for i in range(1000, 3000):
    i = str(i)
    if ((int(i[0])%2==0) and (int(i[1])%2==0) and (int(i[2])%2==0) and (int(i[3])%2==0) ):
        answer.append(i)

print(','.join(answer))

