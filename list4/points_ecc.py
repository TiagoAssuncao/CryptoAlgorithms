#!/usr/bin/env python3
"""Implementation to list points on ecc."""

def find_points(a, b, p):
    """docstring for find_points.

    Search all points on given ecc.
    """
    for i in range(p):
        for j in range(p):
            


if __name__ == "__main__":
    a = input("Digite o coeficiente a: ")
    b = input("Digite o coeficiente b: ")
    p = input("Digite o número primo p: ")

    points_on_ecc = find_points(a, b, p)
