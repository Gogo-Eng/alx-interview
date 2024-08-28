#!/usr/bin/python3
'''
that returns a list of lists of integers
representing the Pascal’s triangle of n:
'''


def pascal_triangle(n):
    '''
    the pascal triangle
    '''
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        row = [1]  # First element is always 1
        for j in range(1, i):
            # Add the sum of the two numbers above this position
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Last element is always 1
        triangle.append(row)

    return triangle
