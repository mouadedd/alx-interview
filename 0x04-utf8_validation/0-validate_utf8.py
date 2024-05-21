#!/usr/bin/python3
"""utf-8 validation"""
# 0-127
# 192 -223
# 224-239
# 240 -247


def validUTF8(data):
    index = 0
    while index < len(data):
        # Check if the current byte is within the valid ranges
        if data[index] < 128:  # 1-byte sequence
            index += 1
        elif 192 <= data[index] <= 223:  # 2-byte sequence
            if index + 1 < len(data) and 128 <= data[index + 1] <= 191:
                index += 2
            else:
                return False
        elif 224 <= data[index] <= 239:  # 3-byte sequence
            if index + 2 < len(data) and \
            all(128 <= byte <= 191 for byte in data[index + 1:index + 3]):
                index += 3
            else:
                return False
        elif 240 <= data[index] <= 247:  # 4-byte sequence
            if index + 3 < len(data) and \
            all(128 <= byte <= 191 for byte in data[index + 1:index + 4]):
                index += 4
            else:
                return False
        else:
            return False  # Invalid leading byte
    return True
