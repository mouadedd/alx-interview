#!/usr/bin/python3
"""
Main file for testing
"""
import time

start = time.time()

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

end = time.time()
print(f"runtime is {end - start} seconds")
