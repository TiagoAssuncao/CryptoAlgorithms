#!/usr/bin/env python3
"""Calcules if a number is prime from the method od Miller Rabin"""
import sys


def find_k_q(n):
    for q in range(1, sys.maxsize, 2):
        k = 1
        resp = 0

        while resp < n:
            resp = ((2**k) * q) + 1
            if resp == n:
                return k, q
            print(q, k)
            k += 1


def testing(k, q, n, a):
    resp = ((a ** q) % n)
    if resp == 1:
        return False

    for j in range(k):
        resp = ((a ** ((2 ** j) * q)) % n)
        if resp == n - 1:
            return False

    return True


if __name__ == "__main__":
    n = int(input("Digite o numero n a ser verificado: "))
    if (n%2 == 0) and (n != 2):
        print("O numero é composto")
        exit()

    k, q = find_k_q(n)
    is_composite = False
    for a in range(1, n):
        resp = testing(k, q, n, a)
        if resp is True:
            is_composite = True

    if is_composite:
        print("O número é composto")
    else:
        prob = (0.25)**(n-1)
        print("O número é primo com a probabilidade: ", prob)
