def calculaRetangulos(n):
    soma = 0
    i = n
    j = n

    while i != 0:
        soma += i-1

        for _ in range(n-1):
            soma += j
            j += 1

        i -= 1
        j = i

    print("retangulos", soma)


def calculaQuadrados(n):
    soma = 0
    while n != 0:
        soma += n**2
        n -= 1

    print("quadrados", soma)


calculaQuadrados(5)
calculaRetangulos(3)
