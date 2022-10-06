valor = int(input())

if 0 < valor < 1000000:
    print(valor)

    notas = valor // 100
    valor = valor % 100
    print(f"{notas} nota(s) de R$ 100,00")

    notas = valor // 50
    valor = valor % 50
    print(f"{notas} nota(s) de R$ 50,00")

    notas = valor // 20
    valor = valor % 20
    print(f"{notas} nota(s) de R$ 20,00")

    notas = valor // 10
    valor = valor % 10
    print(f"{notas} nota(s) de R$ 10,00")

    notas = valor // 5
    valor = valor % 5
    print(f"{notas} nota(s) de R$ 5,00")

    notas = valor // 2
    valor = valor % 2
    print(f"{notas} nota(s) de R$ 2,00")

    notas = valor // 1
    valor = valor % 1
    print(f"{notas} nota(s) de R$ 1,00")
