#!/usr/bin/python3
"""module min operation"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result 
    in exactly n H characters in the file.

    :param n: int - the desired number of H characters
    :return: int - the minimum number of operations required
    """
    if n <= 1:
        return 0
    operations = 0
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            operations += 1
        else:
            n -= 1
            operations += 1
    return int(operations)
