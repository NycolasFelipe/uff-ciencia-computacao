valores = input()

valorA = float(valores.split(" ")[0])
valorB = float(valores.split(" ")[1])
valorC = float(valores.split(" ")[2])

ladoA = 0
ladoB = 0
ladoC = 0

if valorA >= valorB and valorA >= valorC:
    ladoA = valorA
    ladoB = valorB
    ladoC = valorC
elif valorB >= valorA and valorB >= valorC:
    ladoA = valorB
    ladoB = valorA
    ladoC = valorC
elif valorC >= valorA and valorC >= valorB:
    ladoA = valorC
    ladoB = valorA
    ladoC = valorB

if ladoA >= ladoB + ladoC:
    print("NAO FORMA TRIANGULO")
else:
    if ladoA**2 == ladoB**2 + ladoC**2:
        print("TRIANGULO RETANGULO")
    if ladoA**2 > ladoB**2 + ladoC**2:
        print("TRIANGULO OBTUSANGULO")
    if ladoA**2 < ladoB**2 + ladoC**2:
        print("TRIANGULO ACUTANGULO")
    if ladoA == ladoB and ladoB == ladoC:
        print("TRIANGULO EQUILATERO")

    testeIsoscelesA = ladoA == ladoB and ladoA != ladoC
    testeIsoscelesB = ladoB == ladoC and ladoB != ladoA
    testeIsoscelesC = ladoC == ladoA and ladoC != ladoB

    if testeIsoscelesA or testeIsoscelesB or testeIsoscelesC:
        print("TRIANGULO ISOSCELES")
