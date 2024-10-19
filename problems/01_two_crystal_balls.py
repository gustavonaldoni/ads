"""
Given two crystal balls that will break if dropped from a high enough distance, 
determine the exact height in which they will break in the most optimized way.
"""

import math


def two_crystal_balls(array: list[bool]) -> int:
    array_length = len(array)
    jump_distance = int(math.sqrt(array_length))

    for i in range(0, array_length, jump_distance):
        if array[i]:
            break

    i -= jump_distance
    
    for j in range(i, j <= i + jump_distance):
        if array[j]:
            return j
    
    return -1
