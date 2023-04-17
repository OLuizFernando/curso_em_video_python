n = int(input('Digite um número inteiro: '))
for c in range(1, 11):
    print('{} x {:02} = {:02}'.format(n, c, n * c))