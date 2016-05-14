#!/usr/bin/env python3
"""Cipher Feedback(CFB) Implamatation."""

def cfb():
    plains_texts = []
    plains_texts.append(0x00112233445566778899AABBCCDDEEF4)
    plains_texts.append(0x00112233445566778899AABBCCDDEEF5)
    plains_texts.append(0x00112233445566778899AABBCCDDEEF6)

    key = 0x000102030405060708090A0B0C0D0E0F

    cipher_texts = cfb_encrypt()
    descrypt_texts = cfb_decryption()

if __name__ == "__main__":
    cfb()
