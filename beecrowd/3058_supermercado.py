n = int(input())
valores = []
maior = 0
preco = 0

for _ in range(n):
    valor = input().split()
    p = float(valor[0])
    g = int(valor[1])
    valores += [p, g/p, g]

for i in range(1, len(valores), 3):
    if valores[i] > maior:
        maior = valores[i]
        preco = valores[i-1]
        grama = valores[i+1]

resultado = (1000/grama)*preco
print(f"{format(resultado, '.2f')}")
