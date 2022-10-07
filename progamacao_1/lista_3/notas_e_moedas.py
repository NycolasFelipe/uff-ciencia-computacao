valor = float(input())
resto = valor * 100

# notas
notas_100 = resto // 10000
resto %= 10000

notas_50 = resto // 5000
resto %= 5000

notas_20 = resto // 2000
resto %= 2000

notas_10 = resto // 1000
resto %= 1000

notas_5 = resto // 500
resto %= 500

notas_2 = resto // 200
resto %= 200

# moedas
moedas_1 = resto // 100
resto %= 100

moedas_50 = resto // 50
resto %= 50

moedas_25 = resto // 25
resto %= 25

moedas_10 = resto // 10
resto %= 10

moedas_05 = resto // 5
resto %= 5

moedas_01 = resto // 1
resto %= 1

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
