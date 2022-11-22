while True:
    try:
        A, B, C = map(int, input().split())

        if A+B+C == 0 or A+B+C == 3:
            print("*")
        else:
            valores = [A, B, C]
            valores_letras = ["A", "B", "C"]

            for i in range(len(valores)):
                diferente = 0
                for j in range(len(valores)):
                    if i != j and valores[i] != valores[j]:
                        diferente += 1

                if diferente == 2:
                    print(valores_letras[i])
                    break

    except EOFError:
        break
