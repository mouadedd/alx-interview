#!/usr/bin/python3
"""utf-8 validation"""
# 0-127
# 192 -223
# 224-239
# 240 -247

def validUTF8(data):
    result = True
    for i in data:
        if i > 127:
            result = False
            break
    return result
