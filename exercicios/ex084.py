lista = []
pessoas = []
tot = 0
while True:
    tot += 1
    print(f'CADASTRO DA {tot}° PESSOA')
    print('-' * 22)
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso em Kg: ')))
    lista.append(pessoas[:])
    pessoas.clear()
    resp = str(input('Quer Continuar? [S/N] '))
    print('-' * 22)
    if resp in 'Nn':
        break
print(f'Total de pessoas cadastradas: {tot}')
print('Lista de pessoas PESADAS: ', end='')
for p in lista:
    if p[1] >= 90:
        print(f'[{p[0]}, {p[1]} Kg]', end=' ')
print('\nLista de pessoas LEVES: ', end='')
for p in lista:
    if p[1] <= 60:
        print(f'[{p[0]}, {p[1]} Kg]', end=' ')