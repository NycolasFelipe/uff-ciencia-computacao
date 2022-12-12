dias = int(input())

ano = (dias // 365)
mes = (dias % 365) // 30
dia = (dias % 365) % 30

print(str(ano)+" ano(s)\n"+str(mes)+" mes(es)\n"+str(dia)+" dia(s)")
