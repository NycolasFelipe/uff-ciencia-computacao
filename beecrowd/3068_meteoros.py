testando = True
cont = 0

while testando:
    coordenadas = input()
    x1 = int(coordenadas.split()[0])
    y1 = int(coordenadas.split()[1])
    x2 = int(coordenadas.split()[2])
    y2 = int(coordenadas.split()[3])

    if x1+y1+x2+y2 == 0:
        testando = False
    else:
        num_meteoritos = int(input())
        meteoritos_fazenda = 0
        cont += 1

        for i in range(num_meteoritos):
            meteorito_coords = input()
            meteorito_x = int(meteorito_coords.split()[0])
            meteorito_y = int(meteorito_coords.split()[1])

            if x1 <= meteorito_x <= x2:
                if y1 >= meteorito_y >= y2:
                    meteoritos_fazenda += 1

        print(f"Teste {cont}")
        print(meteoritos_fazenda)
