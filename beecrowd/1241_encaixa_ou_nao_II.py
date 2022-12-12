n = int(input())


def linha_contem_valor(linha, teste):
    for i in range(len(teste)):
        linha_valor = linha[len(linha)-len(teste)+i]
        if teste[i] != linha_valor:
            return False
    return True


for _ in range(n):
    linha, teste = input().split()
    encaixa = linha_contem_valor(linha, teste)

    if encaixa:
        print("encaixa")
    else:
        print("nao encaixa")
