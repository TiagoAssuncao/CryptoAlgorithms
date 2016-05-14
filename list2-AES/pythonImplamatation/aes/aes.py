#!/usr/bin/env python3
"""AES Implamatation."""
from keyexpansion import key_expansion
from encryption import encryption
from decryption import decryption

def main():
    key = 0x000102030405060708090A0B0C0D0E0F
    plain = 0x00112233445566778899AABBCCDDEEFF
    expanded_key = key_expansion(key)
    ciphertext = encryption(plain, expanded_key)
    decrypted = decryption(ciphertext, expanded_key)

    if plain == decrypted:
        print("O criptador funcionou corretamente")
    else:
        print("O criptador não funcionou")
if __name__ == "__main__":
        main()
