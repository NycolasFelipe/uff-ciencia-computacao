from random import randint

palavra = input()
palavras = []
tentativa = True
tentativas = 0

while palavra != "0":
    palavras += [palavra]
    palavra = input()

palavra_escolhida = palavras[randint(0, len(palavras)-1)]
palavra_forca = ""


for i in range(len(palavra_escolhida)):
    palavra_forca += "_"
print("Palavra:", palavra_forca)


while tentativa and tentativas < 5:
    letra = input("Informe uma letra: ")
    encontrou_letra = False

    for i in range(len(palavra_escolhida)):
        if letra == palavra_escolhida[i]:
            nova_palavra = ""
            for j in range(len(palavra_escolhida)):
                if letra == palavra_escolhida[j]:
                    nova_palavra += letra
                else:
                    nova_palavra += palavra_forca[j]
            palavra_forca = nova_palavra
            encontrou_letra = True

    print("Palavra:", palavra_forca)

    if palavra_forca == palavra_escolhida:
        print("Você ganhou!")
        tentativa = False

    if not encontrou_letra:
        tentativas += 1
        print("A letra", letra, "não pertence à palavra.")
        print("Quantidade de erros: ", tentativas)
