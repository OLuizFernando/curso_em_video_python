lista = []
aluno = []
notas = []
cont = 0
while True:
    cont += 1
    print('-' * 30)
    print(f'{f"{cont}° ALUNO":^30}')
    print('-' * 30)
    aluno.append(str(input('Nome: ')).strip().title())
    notas.append(float(input('1° Nota: ')))
    notas.append(float(input('2° Nota: ')))
    aluno.append(notas[:])
    lista.append(aluno[:])
    aluno.clear()
    notas.clear()
    resp = str(input('Quer Continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-' * 30)
print(f'N° - NOME              - MÉDIA')
print('-' * 30)
for c in range(1, cont + 1):
    print(f'{c:<5}', end='')
    print(f'{lista[c - 1][0]:<20}', end='')
    print(f'{(lista[c - 1][1][0] + lista[c - 1][1][1]) / 2:<5.2f}')
print('-' * 50)
resp = str(input('Deseja vizualizar alguma nota em específico? [S/N] '))
if resp in 'Ss':
    while True:
        num = int(input('Número do aluno: '))
        print(f'Notas do(a) {lista[num - 1][0]}: {lista[num - 1][1]}')
        resp = str(input('Quer Continuar? [S/N] '))
        if resp in 'Nn':
            break