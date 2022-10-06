notas = input()

nota1 = float(notas.split(" ")[0])
nota2 = float(notas.split(" ")[1])
nota3 = float(notas.split(" ")[2])
nota4 = float(notas.split(" ")[3])

media = (nota1*2 + nota2*3 + nota3*4 + nota4)/10
mediaFormatada = format(media, ".1f")

print(f"Media: {mediaFormatada}")

if media < 5:
    print("Aluno reprovado.")
elif 5 <= media < 6.9:
    print("Aluno em exame.")

    notaExame = float(input())
    notaExameFormatada = format(notaExame, ".1f")
    print(f"Nota do exame: {notaExameFormatada}")

    novaMedia = (media+notaExame)/2
    novaMediaFormatada = format(novaMedia, ".1f")

    if novaMedia >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print(f"Media final: {novaMediaFormatada}")

elif media >= 7:
    print("Aluno aprovado.")
