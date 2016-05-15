#!/usr/bin/env python3
"""Cipher Feedback(CFB) Implamatation."""
import time
from encryption import encryption
from keyexpansion import key_expansion

def cfb_encrypt(texts, expanded_key, nonce):
    cipher_texts = []
    inicialization = nonce

    last_text = inicialization
    for i in range(len(texts)):
        text = encryption(last_text, expanded_key)
        text = texts[i] ^ text
        cipher_texts.append(text)
        last_text = text

    return cipher_texts

def cfb_decryption(texts, expanded_key, nonce):
    descrypt_texts = []
    inicialization = nonce

    last_text = inicialization
    for i in range(len(texts)):
        text = encryption(last_text, expanded_key)
        text = text ^ texts[i]
        last_text = texts[i]
        descrypt_texts.append(text)

    return descrypt_texts

def get_nonce():
    current_time = time.time()
    return int(current_time)

def cfb():
    plains_texts = []
    plains_texts.append(0x00112233445566778899AABBCCDDEEF4)
    plains_texts.append(0x00112233445566778899AABBCCDDEEF5)
    plains_texts.append(0x00112233445566778899AABBCCDDEEF6)

    key = 0x000102030405060708090A0B0C0D0E0F
    expanded_key = key_expansion(key)
    nonce = get_nonce()

    cipher_texts = cfb_encrypt(plains_texts, expanded_key, nonce)
    descrypt_texts = cfb_decryption(cipher_texts, expanded_key, nonce)

    if plains_texts == descrypt_texts:
        print("O cifrador de blocos funcionou corretamente")
    else:
        print("O cifrador não funcionou")
if __name__ == "__main__":
    cfb()
