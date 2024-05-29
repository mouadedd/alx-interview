#!/usr/bin/python3
""" 0. N queens """
from sys import argv, exit


def print_usage():
    '''show usage or exit'''
    print("Usage: nqueens N")
    exit(1)


def is_safe(row, col, cords):
    '''make sure cordinations are safe'''
    for cord in cords:
        place = cord[1]
        if (place == col or place + (row - cord[0]) == col
                or place - (row - cord[0]) == col):
            return False
    return True


def find_solutions(n, row, col, cords, possibilities):
    '''finding the solution'''
    if row == n:
        possibilities.append(cords[:])
        return
    while col < n:
        if is_safe(row, col, cords):
            cords.append([row, col])
            find_solutions(n, row + 1, 0, cords, possibilities)
            cords.pop()
        col += 1


if __name__ == '__main__':
    if len(argv) != 2:
        print_usage()

    try:
        n = int(argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    possibilities = []
    find_solutions(n, 0, 0, [], possibilities)

    for key, value in enumerate(possibilities):
        if key == len(possibilities) - 1:
            print(value, end='')
        else:
            print(value)
