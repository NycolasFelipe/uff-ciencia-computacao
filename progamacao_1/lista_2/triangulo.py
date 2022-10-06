lados = input()

ladoA = float(lados.split(" ")[0])
ladoB = float(lados.split(" ")[1])
ladoC = float(lados.split(" ")[2])

testeA = ladoA >= (ladoB + ladoC)
testeB = ladoB >= (ladoA + ladoC)
testeC = ladoC >= (ladoA + ladoB)

if (testeA or testeB or testeC):
    area = (ladoA + ladoB) * (ladoC / 2)
    areaFormatada = format(area, ".1f")
    print(f"Area = {areaFormatada}")

else:
    perimetro = ladoA + ladoB + ladoC
    perimetroFormatado = format(perimetro, ".1f")
    print(f"Perimetro = {perimetroFormatado}")
