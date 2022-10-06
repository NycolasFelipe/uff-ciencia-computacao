from math import *


def resolverEquacao(a, b, c):
    x1 = (-b+sqrt(b**2-4*a*c))/(2*a)
    x2 = (b+sqrt(b**2-4*a*c))/(2*a)
    print(f"Solução: x1={x1}, x2={x2}")


a = int(input())
b = int(input())
c = int(input())

resolverEquacao(a, b, c)
