"""

Question A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following: UP 5 DOWN 3 LEFT 3 RIGHT 2 ¡­ The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program: UP 5 DOWN 3 LEFT 3 RIGHT 2 Then, the output of the program should be: 2

"""
import math
pos = [0,0]
while(True):
    s = input()
    if not s:
        break
    op, step = s.split(" ")
    step = int(step)
    if op == "UP":
        pos[0]+=step
    elif op == "DOWN":
        pos[0]-=step
    elif op == "LEFT":
        pos[1]-=step
    elif op == "RIGHT":
        pos[1]+=step
    else:
        pass

print(str(math.sqrt(pos[0]**2+pos[1]**2)))
