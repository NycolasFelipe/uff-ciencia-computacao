valores = input()

inicialHora = int(valores.split(" ")[0])
inicialMinuto = int(valores.split(" ")[1])
finalHora = int(valores.split(" ")[2])
finalMinuto = int(valores.split(" ")[3])

tempoFinalMinuto = (finalHora*60) + finalMinuto
tempoInicialMinuto = (inicialHora*60) + inicialMinuto

minutosDia = 1440

if (tempoInicialMinuto > tempoFinalMinuto):
    tempoDiferenca = (minutosDia-tempoInicialMinuto)+tempoFinalMinuto
else:
    tempoDiferenca = tempoFinalMinuto-tempoInicialMinuto

duracaoHora = tempoDiferenca // 60
duracaoMinuto = tempoDiferenca % 60

if tempoDiferenca == 0:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print(f"O JOGO DUROU {duracaoHora} HORA(S) E {duracaoMinuto} MINUTO(S)")
