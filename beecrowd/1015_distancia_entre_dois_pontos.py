from math import *

pontoA = input()
pontoB = input()

pontoAX = float(pontoA.split(" ")[0])
pontoAY = float(pontoA.split(" ")[1])

pontoBX = float(pontoB.split(" ")[0])
pontoBY = float(pontoB.split(" ")[1])

distancia = sqrt(((pontoBX-pontoAX)**2)+((pontoBY-pontoAY)**2))

print(round(distancia, 4))
