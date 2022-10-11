while True:
    try:
        qtd_moedas = int(input())
        lista_moedas = []
        soma = 0

        while len(lista_moedas) != qtd_moedas:
            valor_moeda = int(input())
            lista_moedas += [valor_moeda]

        salto_soma = int(input())

        for i in range(len(lista_moedas)-1, -1, -salto_soma):
            soma += lista_moedas[i]

        for i in range(2, soma+1):
            # é primo
            if i == soma:
                print("You're a coastal aircraft, Robbie, a large silver aircraft.")
            # não é primo
            elif soma % i == 0:
                print("Bad boy! I'll hit you.")
                break

    except EOFError:
        break
