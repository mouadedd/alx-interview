#!/usr/bin/python3
"""0. Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix, rotate it 90 degrees clockwise."""

    idx = 0
    for elem in list(zip(*matrix)):
        matrix[idx][:] = elem[::-1]
        idx += 1
