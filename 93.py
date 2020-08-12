"""

Given a string representing a matrix of numbers, return the rows and columns of that matrix.

So given a string with embedded newlines like:

9 8 7
5 3 2
6 6 7
representing this matrix:

    0  1  2
  |---------
0 | 9  8  7
1 | 5  3  2
2 | 6  6  7
your code should be able to spit out:

A list of the rows, reading each row left-to-right while moving top-to-bottom across the rows,
A list of the columns, reading each column top-to-bottom while moving from left-to-right.

"""
class Matrix(object):
    def __init__(self, mat):
        self.rows = [[el for el in r.split(" ")]for r in mat.split("\n")]
        self.cols = [el for el in zip(*self.rows)]

mat = """9 8 7
5 3 2
6 6 7"""
matrix= Matrix(mat)
print (matrix.rows)
print (matrix.cols)