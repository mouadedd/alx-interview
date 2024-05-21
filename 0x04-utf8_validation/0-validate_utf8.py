#!/usr/bin/python3
"""utf-8 validation"""


def validUTF8(data):
    result = True
    for i in data:
        if i > 247:
            result = False
            break
    return result
