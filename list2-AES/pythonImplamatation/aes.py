#!/usr/bin/env python3
"""AES Implamatation."""
from keyexpansion import key_expansion
from sboxes import *

def main():
    key = 0x2b7e151628aed2a6abf7158809cf4f3c
    key = 0x000102030405060708090A0B0C0D0E0F
    expanded_key = key_expansion(key)

if __name__ == "__main__":
        main()
