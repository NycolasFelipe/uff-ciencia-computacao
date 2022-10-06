valores = input()

valorA = int(valores.split(" ")[0])
valorB = int(valores.split(" ")[1])

multiploAB = (valorA % valorB) == 0
multiploBA = (valorB % valorA) == 0

if multiploAB or multiploBA:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
