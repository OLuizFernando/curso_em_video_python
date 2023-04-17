from random import randint


def linha(x):
    print('-' * x)


def maior(x):
    for c in range(0, x):
        lista.append(randint(0, 9))
        print(lista[c], end=' ')
    print(f'\nForam informados {quant} números.')
    print(f'Maior número: {max(lista)}')
    lista.clear()
    linha(27)


lista = []
linha(27)
for c in range(0, 5):
    quant = randint(1, 10)
    maior(quant)