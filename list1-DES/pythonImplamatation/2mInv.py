def modinv(u, v):
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


def calcprint(u, v):
    re = modinv(u, v)
    if re:
        print("Inv: ", u, " mod ", v, " = ", re)
    else:
        print("Inv: ", u, " mod ", v, " Não existe")


def main():
    calcprint(3041, 17331)
    calcprint(213, 21753)
    calcprint(548, 9571)
    calcprint(24573, 68432)

if __name__ == "__main__":
    main()
