r = int(input(), base=16)
g = int(input(), base=16)
b = int(input(), base=16)

etiquetas = 1

g_em_r = (r//g)**2
b_em_g = ((g//b)**2)*g_em_r
etiquetas += g_em_r + b_em_g

print(hex(etiquetas)[2:])
