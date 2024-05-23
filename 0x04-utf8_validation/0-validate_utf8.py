#!/usr/bin/python3
"""utf-8 validation"""
"""
0-127
 192 -223
 224-239
 240 -247
"""


def validUTF8(data):
    def check_sequence(index, num_bytes):
        for i in range(1, num_bytes):
            if index + i >= len(data) or not (128 <= data[index + i] < 192):
                return False
            return True

    index = 0
    while index < len(data):
        byte = data[index]
        if byte < 128:  # 1-byte sequence
            index += 1
        elif 192 <= byte <= 223:  # 2-byte sequence
            if check_sequence(index, 2):
                index += 2
            else:
                return False
        elif 224 <= byte <= 239:  # 3-byte sequence
            if check_sequence(index, 3):
                index += 3
            else:
                return False
        elif 240 <= byte <= 247:  # 4-byte sequence
            if check_sequence(index, 4):
                index += 4
            else:
                return False
        else:
            return False  # Invalid leading byte
    return True


"""
def validUTF8(data):
    '''function to check if data is utf-8 valid'''
    index = 0

    for i in data:
        if index == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                index = 1
            elif i >> 4 == 0b1110:
                index = 2
            elif i >> 3 == 0b11110:
                index = 3
            elif i >> 7 == 0b1:
                return False

        else:
            if i >> 6 != 0b10:  # using the"==" invalide check 8
                return False
            index -= 1

    return index == 0
"""
