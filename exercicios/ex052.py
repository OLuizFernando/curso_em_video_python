n = int(input('Digite um número inteiro: '))
s = 0
for c in range(1, n+1):
    if n % c == 0:
        s = s + 1
if s == 2:
    print(f'{n} é um número PRIMO.')
else:
    print(f'{n} NÃO é um número primo.')