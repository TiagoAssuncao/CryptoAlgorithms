#!/usr/bin/env python3
"""AES Implamatation."""
from keyexpansion import key_expansion


def main():
    key = 0x2b7e151628aed2a6abf7158809cf4f3c
    expanded_key = key_expansion(key)

if __name__ == "__main__":
    main()
