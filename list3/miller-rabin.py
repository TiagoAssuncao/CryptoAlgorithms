#!/usr/bin/env python3
"""Calcules if a number is prime from the method od Miller Rabin"""
import sys
import random

def find_k_q(n):
    for q in range(3, sys.maxsize, 2):
        resp = 0
        k = 1

        while resp < n:
            resp = ((2**k) * q) + 1
            if resp == n:
                return k, q
            k += 1

def testing(k, q, n, a):
    resp = ((a**q)%n)
    if resp == 1:
        return False

    for j in range(k):
        resp = ((a**(2*j*q))%n)
        if resp == n - 1:
            return False

    return True





if __name__ == "__main__":
    n = int(input("Digite o numero n a ser verificado: "))

    k, q = find_k_q(n)
    is_composite = testing(k, q, n, 10)
    print (is_composite)
