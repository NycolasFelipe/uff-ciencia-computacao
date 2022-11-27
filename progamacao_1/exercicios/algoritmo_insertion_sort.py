lista = [int(i) for i in input().split()]


def insertion_sort(lista):
    for i in range(1, len(lista)):
        j = i
        trocou = True

        while j > 0 and trocou:
            if lista[j] < lista[j-1]:
                aux = lista[j]
                lista[j] = lista[j-1]
                lista[j-1] = aux
                j -= 1
            else:
                trocou = False

    return lista


lista = insertion_sort(lista)
print(lista)
