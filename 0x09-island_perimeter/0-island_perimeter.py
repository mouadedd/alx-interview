#!/usr/bin/python3
"""
Create a function def island_perimeter(grid):
that returns the perimeter of the island described in grid:

grid is a list of list of integers:
0 represents water
1 represents land
Each cell is square, with a side length of 1
Cells are connected horizontally/vertically (not diagonally).
grid is rectangular, with its width and height not exceeding 100
The grid is completely surrounded by water
There is only one island (or nothing).
The island doesn’t have “lakes”
(water inside that isn’t connected to the water surrounding the island).
"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    """
    perim = 0
    length = len(grid) - 1
    border = len(grid[0]) - 1

    for local, lista in enumerate(grid):
        for point, land in enumerate(lista):
            if land == 1:
                if point == 0:
                    perim += 1

                    if lista[point + 1] == 0:
                        perim += 1
                elif point == border:
                    if lista[point - 1] == 0:
                        perim += 1

                    perim += 1
                else:
                    if lista[point - 1] == 0:
                        perim += 1

                    if lista[point + 1] == 0:
                        perim += 1

                if local == 0:
                    perim += 1

                    if grid[local + 1][point] == 0:
                        perim += 1
                elif local == length:
                    if grid[local - 1][point] == 0:
                        perim += 1

                    perim += 1
                else:
                    if grid[local - 1][point] == 0:
                        perim += 1

                    if grid[local + 1][point] == 0:
                        perim += 1

    return perim
