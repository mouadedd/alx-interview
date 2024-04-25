#!/usr/bin/python3
""" Pascal Trangle"""


def pascal_triangle(n):
    """ returns a list of lists of integers representing the Pascal’s triangle of n """
    if n <= 0:
        return []
    else:
        tri = []
        for i in range(n):
            if len(tri) == 0:
                tri.append([1])
            else:
                row = [1]
                for j in range(1, len(tri[-1])):
                    row.append(tri[-1][j] + tri[-1][j - 1])
                row.append(1)
                tri.append(row)
        return tri
