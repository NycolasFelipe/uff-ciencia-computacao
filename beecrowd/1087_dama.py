terminou = False

while not terminou:
    x0, y0, xf, yf = map(int, input().split())
    cont = 0

    if x0+y0+xf+yf == 0:
        terminou = True
    else:
        if x0 == xf and y0 == yf:
            print(cont)
        else:
            dist_x = abs(x0-xf)
            dist_y = abs(y0-yf)

            if dist_x == 0 or dist_y == 0:
                cont += 1
            elif dist_x == dist_y:
                cont += 1
            elif dist_x != dist_y:
                cont += 2

            print(cont)
