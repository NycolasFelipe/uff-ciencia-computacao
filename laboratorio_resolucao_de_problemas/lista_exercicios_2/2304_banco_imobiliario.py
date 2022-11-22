i, n = map(int, input().split())
jogadores = ["D", "E", "F"]
dinheiro = [i, i, i]

for _ in range(n):
    operacao = input().split()
    if operacao[0] == "C":
        for i in range(len(jogadores)):
            if operacao[1] == jogadores[i]:
                dinheiro[i] -= int(operacao[2])
                break
    elif operacao[0] == "V":
        for i in range(len(jogadores)):
            if operacao[1] == jogadores[i]:
                dinheiro[i] += int(operacao[2])
                break
    elif operacao[0] == "A":
        for i in range(len(jogadores)):
            if operacao[1] == jogadores[i]:
                dinheiro[i] += int(operacao[3])
            if operacao[2] == jogadores[i]:
                dinheiro[i] -= int(operacao[3])

print(*dinheiro)
