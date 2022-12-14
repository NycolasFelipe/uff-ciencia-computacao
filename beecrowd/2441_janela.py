f1, f2, f3 = map(int, input().split())
folhas = [f1, f1+200, f2, f2+200, f3, (f3+200, 600)[f3+200 > 600]]

for i in range(len(folhas)):
  print(folhas[i])
  # pegar indices pares 
  # comparar o i com indice par e indice par-1
  # e ver se ele esta entre os dois valores

print(folhas)

# largura = 0

# for i in range(1, len(folhas)):
#   distancia = 0
#   if i != len(folhas)-1:
#     distancia = folhas[i]-folhas[i-1]-200
#     if distancia > 0:
#       largura += distancia
#   else:
#     distancia = 600-folhas[i]-200
#   if distancia > 0:
#     largura += distancia

# print(largura)