#!/usr/bin/python3
"""modul"""


def canUnlockAll(boxes):
    """Returns True if all boxes are locked"""
    keys = [0]
    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and new_key < len(boxes):
                keys.append(new_key)
    return len(keys) == len(boxes)
