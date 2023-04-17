cont = totmais18 = totmasc = totfemsub20 = 0
while True:
    idade = 0
    sexo = ''
    resp = ''
    cont += 1
    print('-' * 22)
    print(f'CADASTRO DA {cont}° PESSOA')
    print('-' * 22)
    while idade <= 0:
        idade = int(input('Idade: '))
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    if idade > 18:
        totmais18 += 1
    if sexo == 'M':
        totmasc += 1
    if idade < 20 and sexo == 'F':
        totfemsub20 += 1
    print('-' * 22)
    while resp != 'S' and resp != 'N':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if resp[0] == 'N':
        break
print('-' * 22)
print(f'Total de pessoas com mais de 18 anos: {totmais18}')
print(f'Total de homens: {totmasc}')
print(f'Total de mulheres com menos de 20 anos: {totfemsub20}')