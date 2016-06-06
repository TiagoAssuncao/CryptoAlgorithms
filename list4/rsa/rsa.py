#!/usr/bin/env python3

def e_is_valid(fi_n, e):
    result_gcd = gcd(fi_n, e)
    if result_gcd == 1:
        is_valid = True
    else:
        is_valid = False

    return is_valid

def gcd(x, y):
    while y!=0:
        (x, y)=(y, x%y)
    return x

def calculate_private_key(fi_n, e):
    inverse_of_e = calculate_inverse(e)
    resp = inverse_of_e % fi_n

    return resp

if __name__ == "__main__":
    p = int(input("Entre com o primo p"))
    q = int(input("Entre com o primo q"))
    e = int(input("Entre com a chave e"))

    n = p * q
    fi_n = (p-1)*(q-1)
    if e_is_valid(fi_n, e):
        print("O valor de e é valido")
    else:
        while not e_is_valid(fi_n, e):
            print("O valor de e é invalido")
            e = int(input("Entre com uma chave VALIDA e"))
        print("Este valor de chave é valido")

    d = calculate_private_key(fi_n, e)
