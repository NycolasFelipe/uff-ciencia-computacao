while True:
    try:
        texto = input()
        valores_ascii = []

        # ordem ascendente de frequência
        # se dois caracteres estiverem presentes com a mesma quantidade de frequência,
        # imprima primeiro o caracter que tem valor ASCII maior.

        # adiciona items da forma [valor_ASCII, frequencia_valor] à lista de valores_ascii
        # se já existir um valor igual, acrescenta a frequencia em 1
        for item in texto:
            valor_existe = False

            if len(valores_ascii) > 0:
                for valor in valores_ascii:
                    if valor[0] == ord(item):
                        valor[1] += 1
                        valor_existe = True
            if not valor_existe:
                valores_ascii += [[ord(item), 1]]

        print(valores_ascii)
        # ordenando a lista
        # for i in range(len(valores_ascii)-1, 0, -1):
        #     for j in range(i):
        #         # testando frequencia
        #         # se a frequencia do primeiro for maior que a do segundo,
        #         # inverte a posição dos dois elementos
        #         if valores_ascii[j][1] > valores_ascii[j+1][1]:
        #             valores_ascii[j], valores_ascii[j+1] = \
        #                 valores_ascii[j+1], valores_ascii[j]

        #         # caso a frequencia do primeiro seja igual à do segundo,
        #         # ordena por valor ascii
        #         elif valores_ascii[j][1] == valores_ascii[j+1][1]:
        #             if valores_ascii[j][0] < valores_ascii[j+1][0]:
        #                 valores_ascii[j], valores_ascii[j+1] = \
        #                     valores_ascii[j+1], valores_ascii[j]

        # exibindo os resultados
        for i in valores_ascii:
            print(f"{i[0]} {i[1]}")
        print("")

    except EOFError:
        break
