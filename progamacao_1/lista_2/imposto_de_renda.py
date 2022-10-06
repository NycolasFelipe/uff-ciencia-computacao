renda = float(input())

if renda < 2000:
    print("Isento")
else:
    if 2000.01 <= renda <= 3000:
        imposto = (renda-2000)*0.08

    elif 3000.01 <= renda <= 4500:
        imposto = 1000*0.08
        imposto += (renda-3000)*0.18

    elif renda > 4500:
        imposto = 1000*0.08
        imposto += 1500*0.18
        imposto += (renda-4500)*0.28

    impostoFormatado = format(imposto, ".2f")
    print(f"R$ {impostoFormatado}")
