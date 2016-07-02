#!/usr/bin/env python3
"""Implementation to list points on ecc."""

def calculate_function(a, b, x, y):
    """docstring for calculate_function"""
    first_result = x**3
    second_result = a*x

    result = (first_result + second_result + b)
    return result

def find_points(a, b, p):
    """docstring for find_points.

    Search all points on given ecc.
    """
    for x in range(p):
        for y in range(p):
            


if __name__ == "__main__":
    a = input("Digite o coeficiente a: ")
    b = input("Digite o coeficiente b: ")
    p = input("Digite o número primo p: ")

    points_on_ecc = find_points(a, b, p)
