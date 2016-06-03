#!/usr/bin/env python3
"""Calcules if a number is prime from the method od Miller Rabin"""
import sys

def find_k_q(n):
    for q in range(3, sys.maxsize, 2):
        resp = 0
        k = 1

        while resp < n:
            resp = ((2**k) * q) + 1
            if resp == n:
                return k, q
            k += 1




if __name__ == "__main__":
    n = int(input("Digite o numero n a ser verificado: "))

    k, q = find_k_q(n)
    print (k, q)
