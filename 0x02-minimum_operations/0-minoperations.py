#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """
    In a text file, there is a single character H. Your text editor
    can execute only two operations in this file: Copy All and Paste.
    Given a number n, write a method that calculates the fewest number
    of operations needed to result in exactly n H characters in the file.
    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0
    """
    min_operations = 2
    total_operations = 0
    while n > 1:
        while n % min_operations == 0:
            total_operations += min_operations
            n /= min_operations
        min_operations += 1
    return total_operations
