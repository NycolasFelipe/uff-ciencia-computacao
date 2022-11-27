divisor, nao_divisor, multiplo, nao_multiplo = map(int, input().split())


def encontra_numero(d, nd, m, nm):
    resultado = -1

    if d != nd and m != nm:
        i = d
        f = m

        while i <= f:
            if i % d == 0 and i % nd != 0:
                if m % i == 0 and nm % i != 0:
                    resultado = i
                    break
            i += d

    return resultado


numero = encontra_numero(divisor, nao_divisor, multiplo, nao_multiplo)
print(numero)
