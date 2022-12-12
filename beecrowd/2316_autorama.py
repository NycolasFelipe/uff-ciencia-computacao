def sort_tabela(lista):
    # [numeroCarro, numeroPostos, ordemChegada, numeroVoltas]
    # ordem por numero de voltas
    for i in range(1, len(lista)):
        j = i
        trocou = True
        while j > 0 and trocou:
            if lista[j][3] > lista[j-1][3]:
                lista[j], lista[j-1] = lista[j-1], lista[j]
                j -= 1
            else:
                trocou = False

    # ordem por numero de postos
    for i in range(1, len(lista)):
        j = i
        trocou = True
        while j > 0 and trocou:
            if lista[j][3] == lista[j-1][3]:
                if lista[j][1] > lista[j-1][1]:
                    lista[j], lista[j-1] = lista[j-1], lista[j]
                j -= 1
            else:
                trocou = False

    # ordem por tempo de chegada
    for i in range(1, len(lista)):
        j = i
        trocou = True
        while j > 0 and trocou:
            if lista[j][1] == lista[j-1][1]:
                if lista[j][3] == lista[j-1][3]:
                    if lista[j][2] < lista[j-1][2]:
                        lista[j], lista[j-1] = lista[j-1], lista[j]
                j -= 1
            else:
                trocou = False

    return lista


k, n, m = map(int, input().split())
tabela = [[int(i), 0, 0, 0] for i in range(1, n+1)]

for i in range(m):
    x, y = map(int, input().split())
    if tabela[x-1][1] == y-1:
        tabela[x-1][1] += 1
        tabela[x-1][2] = i

    if tabela[x-1][1] == k:
        tabela[x-1][1] = 0
        tabela[x-1][3] += 1

tabela = sort_tabela(tabela)
print(' '.join(str(i[0]) for i in tabela))
