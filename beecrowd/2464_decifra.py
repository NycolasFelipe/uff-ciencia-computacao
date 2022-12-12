alfabeto = "abcdefghijklmnopqrstuvwxyz"
permutacao = input()

frase_traduzida = ""
frase = input()

for i in range(len(frase)):
    for j in range(len(permutacao)):
        if frase[i] == permutacao[j]:
            frase_traduzida += alfabeto[j]
            break

print(frase_traduzida)
