#!/usr/bin/python3
"""
that returns a list of lists of integers representing the Pascal’s triangle of n:
"""
def pascal_triangle(n):
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

# Let's see how this works with n = 5.

# Initialization:
# triangle = [[1]]
# First Iteration (i = 1):
# Start a new row: row = [1]
# No elements to calculate (inner loop doesn't run).
# End the row: row = [1, 1]
# Add row to triangle: triangle = [[1], [1, 1]]
# Second Iteration (i = 2):
# Start a new row: row = [1]
# Calculate the middle element: row = [1, 2] (since 1 + 1 = 2)
# End the row: row = [1, 2, 1]
# Add row to triangle: triangle = [[1], [1, 1], [1, 2, 1]]
# Third Iteration (i = 3):
# Start a new row: row = [1]
# Calculate the middle elements: row = [1, 3] (since 1 + 2 = 3)
# Continue: row = [1, 3, 3] (since 2 + 1 = 3)
# End the row: row = [1, 3, 3, 1]
# Add row to triangle: triangle = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
# Fourth Iteration (i = 4):
# Start a new row: row = [1]
# Calculate the middle elements: row = [1, 4] (since 1 + 3 = 4)
# Continue: row = [1, 4, 6] (since 3 + 3 = 6)
# Continue: row = [1, 4, 6, 4] (since 3 + 1 = 4)
# End the row: row = [1, 4, 6, 4, 1]
# Add row to triangle: triangle = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
# This process continues until all rows up to the nth row have been generated.
