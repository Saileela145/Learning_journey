"""
Function: linear_search
Description: Searches for target in list and returns index.
Input: list, target value
Output: index or -1
"""

def linear_search(num, target):
    for i, value in enumerate(num):
        if value == target:
            return i
    return -1
