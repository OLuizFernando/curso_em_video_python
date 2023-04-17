from random import randint
numeros = []


def sorteio():
    for c in range(0, 5):
        numeros.append(randint(0, 10))
        print(numeros[c], end=' ')
    print()


def somapar():
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    print(f'{numeros} = {soma}')


print('Sorteando 5 números:')
sorteio()
print('Somando os PARES:')
somapar()