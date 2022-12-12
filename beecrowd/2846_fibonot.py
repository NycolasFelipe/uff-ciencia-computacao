k = int(input())

# termo 1 e 2
n1 = 1
n2 = 0

# index e valor a ser testado
index = 0
valor = 1

while index < k:
    n1 += n2
    n2 += n1

    if n1 > valor:
        valor += 1
        if n1 != valor:
            index += 1
            n1 = 1
            n2 = 0

    if n2 > valor:
        valor += 1
        if n2 != valor:
            index += 1
            n1 = 1
            n2 = 0

print(valor)
