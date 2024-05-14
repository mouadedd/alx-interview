#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""
from sys import stdin


status = {'200': 0, '301': 0, '400': 0, '401': 0,
          '403': 0, '404': 0, '405': 0, '500': 0}
size = 0
number = 0


try:
    for line in stdin:
        lines = line.split(" ")
        if len(lines) > 4:
            res = lines[-2]
            comp = int(lines[-1])
            if res in status.keys():
                status[res] += 1
            size += comp
            number += 1

        if number == 10:
            number = 0
            print('File size: {}'.format(size))
            for key, value in sorted(status.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))
except Exception as err:
    pass

finally:
    print('File size: {}'.format(size))
    for key, value in sorted(status.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
