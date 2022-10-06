n = int(input())
teste = 0
letras = ["A", "B", "C", "D", "E"]
senha = ""

while n != 0:
    teste += 1

    # lista na forma
    # [[["A", 1, 2], ["B", 3, 4]], [["A", 2, 3], ["B", 4, 5]]]
    associacoes = []

    # lista na forma
    # [[digitos_linha_1], [digitos_linha_2], etc]
    # [[C, B, E, A, E, C], [A, C, B, E, A, B]] por exemplo
    digitos = []

    for _ in range(n):
        associacao = []
        digito = []

        linha = input().split()
        cont_digitos = 0

        for i in range(0, 10, 2):
            associacao += [[letras[cont_digitos], linha[i], linha[i+1]]]
            cont_digitos += 1
        associacoes += [associacao]

        for i in range(10, 16, 1):
            digito += [linha[i]]
        digitos += [digito]

    # substituindo as letras por seus respectivos digitos na ordem em que aparecem
    # exemplo:
    # ["A", "B", "C", "D", "E"] entrada
    # ['39', '08', '24', '17', '24', '39'] saída
    teste_digitos = []
    for i in range(n):
        for digito in digitos[i]:
            for item in associacoes[i]:
                if digito == item[0]:
                    teste_digitos += [item[1]+item[2]]

    # descobrindo a senha por intersecao
    for i in range(0, 6):
        for num_a in teste_digitos[i]:
            for num_b in teste_digitos[i+6]:
                if num_a == num_b:
                    senha += num_a + " "

    print(f"Teste {teste}")
    print(senha)

    n = int(input())
