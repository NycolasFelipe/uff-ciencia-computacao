num, distancia = map(int, input().split())
postos = list(map(int, input().split()))
consegue = "S"

for i in range(num):
    if i == num-1:
        if 42195 > postos[i]+distancia:
            consegue = "N"
        break
    elif postos[i+1] > postos[i]+distancia:
        consegue = "N"
        break

print(consegue)
