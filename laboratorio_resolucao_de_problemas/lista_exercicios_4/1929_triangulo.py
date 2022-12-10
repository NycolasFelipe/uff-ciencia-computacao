def trianguloValido(lados):
  for i in range(len(lados)):
    lado_a = lados[i]

    for j in range(len(lados)):
      lado_b = lados[j]

      for k in range(len(lados)):
        lado_c = lados[k]
        
        if i != j and i != k and j != k:
          if lado_a < lado_b + lado_c:
            if lado_b < lado_a + lado_c:
              if lado_c < lado_a + lado_b:
                return True
  return False

lados = [int(i) for i in input().split()]
valido = trianguloValido(lados)

if valido:
  print("S")
else:
  print("N")