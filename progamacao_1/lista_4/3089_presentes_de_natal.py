n = int(input())

while n != 0:
    m = [int(i) for i in input().split()]
    lista = []

    for i in range(n):
        lista += [m[i] + m[len(m)-1-i]]

    if lista[0] < lista[-1]:
        lista[0], lista[-1] = lista[-1], lista[0]

    print(lista[0], lista[-1])
    n = int(input())
