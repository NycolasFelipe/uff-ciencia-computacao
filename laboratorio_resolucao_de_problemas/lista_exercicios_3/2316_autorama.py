k, n, m = map(int, input().split())
tabela = [[int(i), 0, 0] for i in range(1, n+1)]

for i in range(m):
    x, y = map(int, input().split())
    if tabela[x-1][1] == y-1:
        tabela[x-1][1] += 1
        tabela[x-1][2] = i


def sort_tabela(lista):
    for i in range(1, len(lista)):
        j = i
        trocou = True
        while j > 0 and trocou:
            if lista[j][1] > lista[j-1][1]:
                lista[j], lista[j-1] = lista[j-1], lista[j]
                j -= 1
            else:
                trocou = False

    for i in range(1, len(lista)):
        j = i
        trocou = True
        while j > 0 and trocou:
            if lista[j][1] == lista[j-1][1] and lista[j][2] < lista[j-1][2]:
                lista[j], lista[j-1] = lista[j-1], lista[j]
                j -= 1
            else:
                trocou = False

    return lista


print(' '.join(str(i[0]) for i in tabela))
