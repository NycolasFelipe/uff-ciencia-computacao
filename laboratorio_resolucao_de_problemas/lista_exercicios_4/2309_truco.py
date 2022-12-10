def calcula_valor_carta(carta):
  valor = carta
  if carta == 12:
    valor = 8
  elif carta == 11:
    valor = 9
  elif carta == 13:
    valor = 10
  elif carta == 1:
    valor = 11
  elif carta == 2:
    valor = 12
  elif carta == 3:
    valor = 13
  return valor 

def calcula_maior_carta(carta_a, carta_b):
  valor_a, valor_b = 0, 0
  valor_a = calcula_valor_carta(carta_a)
  valor_b = calcula_valor_carta(carta_b)

  if valor_b > valor_a:
    return "carta_b"
  else:
    return "carta_a"


rodadas = int(input())
placar_a, placar_b = 0, 0

for _ in range(rodadas):
  pontos_a, pontos_b = 0, 0
  cartas = [int(i) for i in input().split()]
  jogador_a = cartas[:3]
  jogador_b = cartas[3:]

  for i in range(3):
    maior_carta = calcula_maior_carta(jogador_a[i], jogador_b[i])
    if maior_carta == "carta_a":
      pontos_a += 1
    else:
      pontos_b += 1
  
  if pontos_a > pontos_b:
    placar_a += 1
  else:
    placar_b += 1

print(placar_a, placar_b)
