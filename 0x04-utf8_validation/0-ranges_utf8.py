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
            if not index + i >= len(data) or (128 <= data[index + i] <= 191):
                return True
        return False

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
