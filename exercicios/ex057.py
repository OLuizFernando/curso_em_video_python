sexo = ''
while sexo.upper() != 'F' and sexo.upper() != 'M':
    sexo = str(input('Digite seu sexo [M/F]: '))
    if sexo.upper() != 'F' and sexo.upper() != 'M':
        print('Valor incorreto. Tente novamente.')