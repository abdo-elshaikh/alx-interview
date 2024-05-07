#!/usr/bin/python3
"""module min operation"""


def minOperations(n):
    """return impossible to achieve """
    if n <= 1:
        return n

    operations = 0
    clipboard = 1
    buffer = 0

    while clipboard < n:
        if n % clipboard == 0:
            buffer = clipboard
            operations += 1
        clipboard += buffer
        operations += 1

    return operations
