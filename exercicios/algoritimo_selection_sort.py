lista = [int(i) for i in input().split()]


def selection_sort(lista):
    for i in range(len(lista)):
        j = i
        menor = j

        for k in range(j+1, len(lista)):
            if lista[k] < lista[menor]:
                menor = k

        if j != menor:
            aux = lista[j]
            lista[j] = lista[menor]
            lista[menor] = aux

    return lista


lista = selection_sort(lista)
print(lista)
