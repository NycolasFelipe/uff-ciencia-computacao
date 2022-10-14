n = int(input())

while n != 0:
    pontos_a = 0
    pontos_b = 0

    for _ in range(n):
        valor_a, valor_b = map(int, input().split())
        if valor_a > valor_b:
            pontos_a += 1
        elif valor_a < valor_b:
            pontos_b += 1

    print(f"{pontos_a} {pontos_b}")
    n = int(input())
