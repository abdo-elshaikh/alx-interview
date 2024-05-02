#!/usr/bin/python3
"""modul"""


def canUnlockAll(boxes):
    """
    canUnlockAll
    """
    keys = [0]
    n = len(boxes)
    for i in range(0, n - 1):
        for j in boxes[i]:
            if j not in keys:
                keys.append(j)
    for i in range(0, n):
        if i not in keys:
            return False
    return True
