linha = input()
linha_vogais = []


def encontra_vogais(linha):
    linha_vogais = []
    for i in range(len(linha)):
        if linha[i] == "a" or \
                linha[i] == "e" or \
                linha[i] == "i" or \
                linha[i] == "o" or \
                linha[i] == "u":
            linha_vogais += linha[i]
    return linha_vogais


def testa_linha_espelhada(linha):
    for i in range(len(linha)):
        linha_direita = linha[len(linha)-1-i]
        if linha[i] != linha_direita:
            return False
    return True


linha_vogais = encontra_vogais(linha)
linha_valida = testa_linha_espelhada(linha_vogais)

if linha_valida:
    print("S")
else:
    print("N")
