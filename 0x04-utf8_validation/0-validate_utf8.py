#!/usr/bin/python3
"""utf-8 validation"""
"""
0-127
 192 -223
 224-239
 240 -247
"""


def validUTF8(data):
    """function to check if data is utf-8 valid"""
    index = 0

    for i in data:
        if index == 0:
            if i >> 7 == 0b1:
                return False
            elif i >> 5 == 0b110 or i >> 5 == 0b1110:
                index = 1
            elif i >> 4 == 0b1110:
                index = 2
            elif i >> 3 == 0b11110:
                index = 3

        else:
            if i >> 6 != 0b10:
                return False
            index -= 1

    return index == 0
