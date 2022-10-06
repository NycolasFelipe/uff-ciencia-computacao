valor = float(input())
resto = valor

# notas
notas_100 = resto // 100
resto %= 100

notas_50 = resto // 50
resto %= 50

notas_20 = resto // 20
resto %= 20

notas_10 = resto // 10
resto %= 10

notas_5 = resto // 5
resto %= 5

notas_2 = resto // 2
resto %= 2

# moedas
moedas_1 = resto // 1
resto %= 1

moedas_50 = resto // 0.50
resto %= 0.50

moedas_25 = resto // 0.25
resto %= 0.25

moedas_10 = resto // 0.10
resto %= 0.10

moedas_05 = resto // 0.05
resto %= 0.05

moedas_01 = resto // 0.01
resto %= 0.01

# print notas
print("NOTAS:")
print(f"{int(notas_100)} nota(s) de R$ 100.00")
print(f"{int(notas_50)} nota(s) de R$ 50.00")
print(f"{int(notas_20)} nota(s) de R$ 20.00")
print(f"{int(notas_10)} nota(s) de R$ 10.00")
print(f"{int(notas_5)} nota(s) de R$ 5.00")
print(f"{int(notas_2)} nota(s) de R$ 2.00")

# print moedas
print("MOEDAS:")
print(f"{int(moedas_1)} moeda(s) de R$ 1.00")
print(f"{int(moedas_50)} moeda(s) de R$ 0.50")
print(f"{int(moedas_25)} moeda(s) de R$ 0.25")
print(f"{int(moedas_10)} moeda(s) de R$ 0.10")
print(f"{int(moedas_05)} moeda(s) de R$ 0.05")
print(f"{int(moedas_01)} moeda(s) de R$ 0.01")
