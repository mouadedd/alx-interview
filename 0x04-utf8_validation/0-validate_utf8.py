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
    def check_sequence(index, num_bytes):
        """checking the sequence fall range"""
        for i in range(1, num_bytes):
            if index + i >= len(data) or not (128 <= data[index + i] <= 191):
                return False
        return True

    index = 0
    while index < len(data):
        byte = data[index]
        if byte < 128:
            index += 1
        elif 192 <= byte <= 223:
            if check_sequence(index, 2):
                index += 2
            else:
                return False
        elif 224 <= byte <= 239:
            if check_sequence(index, 3):
                index += 3
            else:
                return False
        elif 240 <= byte <= 247:
            if check_sequence(index, 4):
                index += 4
            else:
                return False
        else:
            return False
    return True
