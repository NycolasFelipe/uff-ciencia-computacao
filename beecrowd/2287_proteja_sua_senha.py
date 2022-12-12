n = int(input())
teste = 0
senha = ""

while n != 0:
    teste += 1

    temp = []
    for _ in range(n):
        temp += input().split()

    for i in range(10, 16):
        indice = (ord(temp[i])-ord("A"))*2
        digito_A = temp[indice]+temp[indice+1]
        digitos = ["*" for _ in range(n)]
        digitos[0] = digito_A

        for j in range(1, n):
            n_indice = 16*j+i
            indice = (ord(temp[n_indice])-ord("A"))*2
            digito_B = temp[16*j+indice]+temp[16*j+indice+1]
            digitos[j] = digito_B

        indice = 1
        for j in range(1, n):
            if digito_A[0] == digitos[j][0]:
                indice += 1
            if digito_A[0] == digitos[j][1]:
                indice += 1

        if indice == n:
            senha += digito_A[0] + " "
        else:
            senha += digito_A[1] + " "

    print(f"Teste {teste}")
    print(senha)
    print("")

    senha = ""
    n = int(input())
