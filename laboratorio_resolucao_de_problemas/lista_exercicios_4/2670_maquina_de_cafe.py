def calcula_tempo(andar, andares):
  total_minutos = 0
  for i in range(len(andares)):
    if i != andar:
      for _ in range(abs(andar-i)):
        total_minutos += andares[i]*2
  return total_minutos

def calcula_menor_tempo(tempos):
  tempo = tempos[0]
  for i in range(len(tempos)):
    if tempos[i] < tempo:
      tempo = tempos[i]
  return tempo

andar_a = int(input())
andar_b = int(input())
andar_c = int(input())

andares = [andar_a, andar_b, andar_c]
tempos = []
menor_tempo = 0

for i in range(len(andares)):
  tempos += [calcula_tempo(i, andares)]

menor_tempo = calcula_menor_tempo(tempos)
print(menor_tempo)
