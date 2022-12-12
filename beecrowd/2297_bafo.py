rodadas = int(input())
teste = 0

while rodadas != 0:
  pts_a, pts_b = 0, 0
  teste += 1
  print(f"Teste {teste}")

  for _ in range(rodadas):
    aldo, beto = map(int, input().split())
    pts_a += aldo
    pts_b += beto
  
  if pts_a > pts_b:
    print("Aldo")
  else:
    print("Beto")
  print("")
  
  rodadas = int(input())