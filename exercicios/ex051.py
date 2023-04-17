n = int(input('Digite um número inteiro: '))
r = int(input('Digite a razão da PA: '))
d = n + (10 - 1) * r
for c in range(n, d + r, r):
    print(c)