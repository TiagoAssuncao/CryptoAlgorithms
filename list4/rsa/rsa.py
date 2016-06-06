#!/usr/bin/env python3

def calculate_inverse(u, v):
    u1, u3, v1, v3, ite = 1, u, 0, v, 0

    while(v3 != 0):
        q = u3 // v3

# t1 and t3 be temp variables to stores the values of coeficients and
# swap with v1
        t3 = u3 % v3
        t1 = u1 + q * v1

        u1, v1, u3, v3, ite = v1, t1, v3, t3, ite + 1

    if(u3 != 1):
        return 0

    if((ite % 2) != 0):
        inv = v - u1
    else:
        inv = u1

    return inv

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
    inverse_of_e = calculate_inverse(e, fi_n)

    return inverse_of_e

def decrip(PU):
    file_text = get_file()
    pass


def crip(PU):
    file_text = get_file()
    pass

if __name__ == "__main__":
    p = int(input("Entre com o primo p: "))
    q = int(input("Entre com o primo q: "))
    e = int(input("Entre com a chave e: "))

    n = p * q
    fi_n = (p-1)*(q-1)
    while not e_is_valid(fi_n, e):
        print("O valor de e é invalido")
        e = int(input("Entre com uma chave VALIDA e"))
    print("Este valor de chave é valido")

    d = calculate_private_key(fi_n, e)
    PU = [e, n]
    PR = [d, n]

    option = input("Deseja criptografar ou descriptografar? (c/d)")
    if option == 'c':
        crip(PU)
    elif option == 'd':
        decript(PR)
    else:
        print("Opcao desconhecida")
