from math import *

coeficientes = input()

A = float(coeficientes.split(" ")[0])
B = float(coeficientes.split(" ")[1])
C = float(coeficientes.split(" ")[2])

delta = B**2 - 4*A*C

if A == 0 or delta < 0:
    print("Impossivel calcular")

else:
    R1 = (-B + sqrt(delta))/(2*A)
    R1Final = format(R1, ".5f")

    R2 = (-B - sqrt(delta))/(2*A)
    R2Final = format(R2, ".5f")

    print(f"R1 = {R1Final}\nR2 = {R2Final}")
