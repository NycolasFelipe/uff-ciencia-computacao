n = int(input())
cont_teste = 0

while n != 0:
    jogador1 = input()
    jogador2 = input()
    cont_teste += 1

    print(f"Teste {cont_teste}")

    while n > 0:
        mao_jogadores = input()
        mao_jogador1 = int(mao_jogadores.split()[0])
        mao_jogador2 = int(mao_jogadores.split()[1])

        # é par
        if (mao_jogador1 + mao_jogador2) % 2 == 0:
            print(jogador1)
        # é ímpar
        else:
            print(jogador2)
        n -= 1

    print("")
    n = int(input())