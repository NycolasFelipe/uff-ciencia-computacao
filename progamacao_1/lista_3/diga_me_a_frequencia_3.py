while True:
    try:
        texto = input()
        valores_ascii = []

        # armazenando caracteres na lista valores_ascii na
        # forma [[frequencia, valor]]
        # ex.: [[1, 94], [4, 80]]
        for char in texto:
            if len(valores_ascii) != 0:
                valor_existe = False
                index = 0

                for i in range(len(valores_ascii)):
                    if ord(char) == valores_ascii[i][1]:
                        valor_existe = True
                        valores_ascii[i][0] += 1
                        index = i

                if not valor_existe:
                    valores_ascii += [[1, ord(char)]]
                    index = len(valores_ascii)-1
            else:
                valores_ascii += [[1, ord(char)]]

        # ordenando por frequencia, e então por valor ascii
        valores_ascii.sort(key=lambda item: (item[0], -item[1]))

        # exibindo o resultado
        for item in valores_ascii:
            print(f"{item[1]} {item[0]}")
        print("")

    except EOFError:
        break
