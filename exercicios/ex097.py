def titulo(x):
    print('-' * (len(x) + 4))
    print(f'{x:^{len(x) + 4}}')
    print('-' * (len(x) + 4))


titulo(str(input('Escreva uma frase: ')).strip().upper())