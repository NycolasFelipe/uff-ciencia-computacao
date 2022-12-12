lista = [int(i) for i in input().split()]


def bubble_sort(lista):
    i = 0
    trocou = True

    while trocou and i < len(lista):
        for j in range(len(lista)-1-i):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
                trocou = True
        i += 1

    return lista


lista = bubble_sort(lista)
print(lista)
