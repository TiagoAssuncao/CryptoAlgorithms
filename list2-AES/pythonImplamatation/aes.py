#!/usr/bin/env python3
"""AES Implamatation."""
from keyexpansion import key_expansion
from encryption import encryption
def main():
    key = 0x000102030405060708090A0B0C0D0E0F
    key = 0x0f1571c947d9e8590cb7add6af7f6798
    plain = 0x00112233445566778899AABBCCDDEEFF
    plain = 0x0123456789abcdeffedcba9876543210
    expanded_key = key_expansion(key)
    ciphertext = encryption(plain, expanded_key)
    decrypted = decryption(ciphertext, expanded_key)

if __name__ == "__main__":
        main()
