n = int(input())
teste = 0
letras = ["A", "B", "C", "D", "E"]

while n != 0:
    senha = ""
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

    # substituindo as letras por seus respectivos digitos na ordem em
    # que aparecem.
    # por exemplo:
    # ["A", "B", "C", "D", "E"] entrada
    # ['39', '08', '24', '17', '24', '39'] saída
    teste_digitos = []
    for i in range(n):
        for digito in digitos[i]:
            for item in associacoes[i]:
                if digito == item[0]:
                    teste_digitos += [item[1]+item[2]]

    # descobrindo a senha
    for i in range(0, 6):
        # acessa o primeiro par de digitos e compara com o restante
        # que estão na mesma posicao
        digito_a = teste_digitos[i]
        digitos = [digito_a]

        for j in range(1, n):
            # acessa o primeiro digito relativo à sua linha de teste
            digito_b = teste_digitos[(j*6)+i]

            # se o numero de testes for maior que 2, armazena os digitos
            # para serem processados mais a frente
            if n > 2:
                digitos += [digito_b]
            # caso contrario sejam somente 2 testes, processa a senha
            # diretamente
            else:
                for num_a in digito_a:
                    for num_b in digito_b:
                        if num_a == num_b:
                            senha += num_a + " "

        # nesse bloco é testado os numeros contidos no primeiro digito
        # teste. esse digito contém 2 numeros, e a senha pode ser somente
        # um dos dois. digitos_copia armazena todos os valores em digitos
        # que contêm o primeiro numero.
        #
        # se o tamanho de digitos_copia for diferente do que digitos, isso
        # quer dizer que o primeiro número não está em todos os dígitos,
        # logo o segundo numero necessariamente faz parte da senha
        if n > 2:
            digitos_copia = []
            for digito in digitos:
                for num in digito:
                    if digito_a[0] == num:
                        digitos_copia += [digito]

            if len(digitos) == len(digitos_copia):
                senha += digito_a[0] + " "
            else:
                senha += digito_a[1] + " "

    print(f"Teste {teste}")
    print(senha)
    print("")

    n = int(input())
