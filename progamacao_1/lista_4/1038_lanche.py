num, qtd = map(int, input().split())
tabela = [4.0, 4.5, 5.0, 2.0, 1.5]
soma = 0

for _ in range(qtd):
    soma += tabela[num-1]

print(f"Total: R$ {format(soma, '.2f')}")
