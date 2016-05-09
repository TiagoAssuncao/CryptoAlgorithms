"""
Program to calculate the arithmetic modular
"""

def sum(a, b):
    c = a ^ b
    return c

def makeVectorMult(a):
    vmult = [a,0,0,0,0,0,0,0]
    for i in range(1, 8):
        var = vmult[i-1]
        if (var & 128) == 128:
            var = ((var - 128 )<< 1)
            var = var ^ 27
        else:
            var = var << 1

        vmult[i] = var

    return vmult

def getIndex(a):
    v = [1, 2, 4, 8, 16, 32, 64, 128]
    ids = []
    cont = 0

    for i in v:
        if(a & i) == i:
            ids.append(cont)

        cont = cont + 1
    return ids

def mult(a, b):
    vmult = makeVectorMult(a)
    ids = getIndex(b)
    values = []

    result = 0
    for i in ids:
        result = result ^ vmult[i]
    return result

def div(a, b):
    resp = -1
    for i in range(0, 256):
        vmult = mult(b, i)
        if (vmult % 27) == 1:
            resp = i
            break
    return mult(a, resp)


def main():
    try:
        a, op, b = input("Operação no formato: a operation b: ").split()
        a, b = int(a), int(b)
    except Exception:
        print("Valores de entrada errados. Abortando")
        return
    resp = -1
    if op is "+":
        resp = sum(a, b)
    elif op is "*":
        resp = mult(a, b)
    elif op is "-":
        resp = sum(a, b)
    elif op is "/":
        resp = div(a, b)

    if resp != -1:
        print(resp)
    else:
        print("Operação não conhecida")

if __name__ == "__main__":
    main()
