#!/usr/bin/python3
""" modul"""


def pascal_triangle(n):
    """
    pascal"""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle


# Test the function
if __name__ == "__main__":
    triangle = pascal_triangle(5)
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))
