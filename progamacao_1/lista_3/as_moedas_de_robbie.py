while True:
    try:
        qtd_moedas = int(input())
        lista_moedas = []
        soma = 0

        while len(lista_moedas) != qtd_moedas:
            valor_moeda = int(input())
            lista_moedas += [valor_moeda]

        salto_soma = int(input())

        for i in range(0, qtd_moedas, salto_soma):
            soma += lista_moedas[i]

        for i in range(2, soma):
            # não é primo
            if soma % i == 0:
                print("Bad boy! I'll hit you.")
                break
            # é primo
            elif i == soma-1:
                print("You're a coastal aircraft, Robbie, a large silver aircraft.")
                jogando = False
    except EOFError:
        break
