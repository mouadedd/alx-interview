#!/usr/bin/python3
"""utf-8 validation"""
# 0-127
# 192 -223
# 224-239
# 240 -247

def validUTF8(data):
    index = 0
    result = True
    for i in data:
        if i > 247:
            result = False
            break
        if 0 <= data[0] <= 127:
            for i in data:
                if i > 127:
                    result = False
        if 192 <= data[0] <= 223:
            for i in data:
                if 192 <= i <= 223 :
                    result = False
        if 224 <= data[0] <= 239:
            for i in data:
                if 224 <= i <= 239 :
                    result = False
        if 240 <= data[0] <= 247:
            for i in data:
                if 240 <= i <= 247 :
                    result = False
    return result
