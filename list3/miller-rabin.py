#!/usr/bin/env python3
"""Calcules if a number is prime from the method od Miller Rabin"""

if __name__ == "__main__":
    n = int(raw_imput("Digite o numero n a ser verificado"))

    k, q = find_k_q(n)
