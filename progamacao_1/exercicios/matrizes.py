def criaMatriz(linhas, colunas):
    return [[0]*colunas for _ in range(linhas)]


def acessaMatrizes(arquivo, dimensoes):
    linha_a = dimensoes[0]
    linha_b = dimensoes[2]

    matrizes = [i[:-1].split() for i in arquivo[1:linha_a+linha_b+1]]
    for i in range(len(matrizes)):
        for j in range(len(matrizes[i])):
            matrizes[i][j] = int(matrizes[i][j])

    resultado = [[], []]
    resultado[0] = matrizes[:linha_a]
    resultado[1] = matrizes[linha_a:]

    return resultado


def matrizInvalida(dimensoes):
    linhas_b = int(dimensoes[2])
    colunas_a = int(dimensoes[1])

    if colunas_a == linhas_b:
        return False
    return True


def multiplicaMatrizes(matriz_a, matriz_b):
    matriz_res = criaMatriz(len(matriz_a), len(matriz_b[0]))

    for i in range(len(matriz_a)):
        for k in range(len(matriz_b[0])):
            soma = 0
            for j in range(len(matriz_a[0])):
                soma += matriz_a[i][j]*matriz_b[j][k]
            matriz_res[i][k] += soma

    return matriz_res


def escreveResultado(resultado, endereco, dimensoes):
    arquivo = open(endereco, 'r')
    linha_a = dimensoes[0]
    linha_b = dimensoes[2]
    dados = arquivo.readlines()[:linha_a+linha_b+1]
    dados += ["resultado\n"]

    for i in range(len(resultado)):
        for j in range(len(resultado[i])):
            dados += [str(resultado[i][j])+" "]
        dados += '\n'
    arquivo.close()

    arquivo = open(endereco, 'w')
    for i in range(len(dados)):
        arquivo.write(dados[i])
    arquivo.close()


def calculaMatriz(endereco):
    arquivo = open(endereco, 'r')
    dados = arquivo.readlines()
    dimensoes = [int(i) for i in dados[0][:-1].split()]

    if matrizInvalida(dimensoes):
        return

    matrizes = acessaMatrizes(dados, dimensoes)
    matriz_a = matrizes[0]
    matriz_b = matrizes[1]

    matriz_res = multiplicaMatrizes(matriz_a, matriz_b)
    escreveResultado(matriz_res, endereco, dimensoes)

    arquivo.close()


calculaMatriz('matrizes.txt')
