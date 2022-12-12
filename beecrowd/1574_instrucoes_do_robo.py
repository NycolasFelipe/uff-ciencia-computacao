n = int(input())


for _ in range(n):
    m = int(input())
    p = 0
    instrucoes = []

    for _ in range(m):
        linha = input().split()
        instrucao = linha[-1]

        if instrucao == "RIGHT":
            p += 1
            instrucoes += ["RIGHT"]
        elif instrucao == "LEFT":
            p -= 1
            instrucoes += ["LEFT"]
        else:
            nova_instrucao = ''
            instrucao_valida = False

            while not instrucao_valida:
                nova_instrucao = instrucoes[int(linha[-1])-1]
                if nova_instrucao == 'RIGHT' or nova_instrucao == 'LEFT':
                    instrucao_valida = True
                    instrucoes += [nova_instrucao]
                else:
                    instrucao = instrucoes[int(linha[-1])-1]

            if nova_instrucao == "RIGHT":
                p += 1
            elif nova_instrucao == "LEFT":
                p -= 1

    print(p)
