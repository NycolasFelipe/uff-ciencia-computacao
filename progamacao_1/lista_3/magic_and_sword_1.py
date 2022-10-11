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

    intersecao = False

    # intersecao na reta paralela a OY passando por x0 e x0+w
    intersecao_oy_x0 = -1
    intersecao_oy_x0_w = -1

    oy_x0 = raio-(x0-cx)**2
    oy_x0_w = raio-(x0+w-cx)**2

    if oy_x0 >= 0:
        intersecao_oy_x0 = cy-sqrt(oy_x0)
    if oy_x0_w >= 0:
        intersecao_oy_x0_w = cy-sqrt(oy_x0_w)

    print(intersecao_oy_x0)

    # intersecao na reta paralela a OX passando por y0 e y0+h
    intersecao_ox_y0 = -1
    intersecao_ox_y0_h = -1

    ox_y0 = raio-(y0-cy)**2
    ox_y0_h = raio-(y0+h-cy)**2

    if ox_y0 >= 0:
        intersecao_ox_y0 = cx-sqrt(ox_y0)
    if ox_y0_h >= 0:
        intersecao_ox_y0_h = cx-sqrt(ox_y0_h)

    # checando se a intersecao ocorre dentro dos limites do retangulo
    if y0 <= intersecao_oy_x0 <= y0+h:
        intersecao = True
    elif y0 <= intersecao_oy_x0+h <= y0+h:
        intersecao = True
    elif x0 <= intersecao_ox_y0 <= x0+w:
        intersecao = True
    elif x0 <= intersecao_ox_y0+w <= x0+w:
        intersecao = True

    print(intersecao)
