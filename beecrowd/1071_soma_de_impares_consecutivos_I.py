x = int(input())
y = int(input())

soma = 0

if x > y:
    temp_x = x
    x = y
    y = temp_x

for i in range(x+1, y):
    if i % 2 != 0:
        soma += i

print(soma)
