from math import sqrt


# testes = int(input())
testes = 1

# magia:
# circulo de centro em cx e cy
# cujo círculo é determinado pelo nivel da magia

# tropas:
# retangulo de coordenada inferior esquerda x0
# e y0, altura h e largura w.

# caso haja intersecao, o dado é determinado
# na tabela, de acordo com o nivel da magia

for i in range(testes):
    # w, h, x0, y0 = map(int, input().split())
    # magia, level, cx, cy = input().split()
    # dano = 0
    # raio = 0

    # # definindo dano e raio da magia
    # if magia == "fire":
    #     dano = 200
    #     if level == 1:
    #         raio = 20
    #     elif level == 2:
    #         raio = 30
    #     elif level == 3:
    #         raio = 50

    # elif magia == "water":
    #     dano = 300
    #     if level == 1:
    #         raio = 10
    #     elif level == 2:
    #         raio = 25
    #     elif level == 3:
    #         raio = 40

    # elif magia == "earth":
    #     dano = 400
    #     if level == 1:
    #         raio = 25
    #     elif level == 55:
    #         raio = 55
    #     elif level == 3:
    #         raio = 70

    # elif magia == "air":
    #     dano = 100
    #     if level == 1:
    #         raio = 18
    #     elif level == 55:
    #         raio = 38
    #     elif level == 3:
    #         raio = 60

    x0 = 2.5
    y0 = 3
    cx = 2
    cy = 2.5
    raio = 1.25

    h = 1
    w = 1

    # checar se a distancia dos vertices até centro-raio é menor do que
    # o raio
