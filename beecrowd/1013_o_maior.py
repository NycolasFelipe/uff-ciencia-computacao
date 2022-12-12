valores = input()

valorA = int(valores.split(" ")[0])
valorB = int(valores.split(" ")[1])
valorC = int(valores.split(" ")[2])

maiorAB = (valorA+valorB+abs(valorA-valorB))/2
maiorBC = (valorB+valorC+abs(valorB-valorC))/2

maiorFinal = (maiorAB+maiorBC+abs(maiorAB-maiorBC))/2
maiorFinalFormatado = format(maiorFinal, ".0f")

print(f"{maiorFinalFormatado} eh o maior")
