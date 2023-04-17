from random import randint
totv = 0
while True:
    jparouimpar = str(input('Par ou ímpar? ')).strip().lower()
    while jparouimpar[0] not in 'pií':
        jparouimpar = str(input('Par ou ímpar? ')).strip().lower()
    if jparouimpar[0] in 'p':
        jparouimpar = 0
        cparouimpar = 1
    elif jparouimpar[0] in 'ií':
        jparouimpar = 1
        cparouimpar = 0
    jnum = int(input('Digite um número: '))
    cnum = randint(1, 10)
    if jparouimpar == 0:
        if (jnum + cnum) % 2 == 0:
            vitoria = True
            totv += 1
        elif (jnum + cnum) % 2 == 1:
            vitoria = False
    elif jparouimpar == 1:
        if (jnum + cnum) % 2 == 0:
            vitoria = False
        elif (jnum + cnum) % 2 == 1:
            vitoria = True
            totv += 1
    print(f'Você jogou \033[34m{jnum}\033[m e eu joguei \033[31m{cnum}\033[m\n{jnum} + {cnum} = {jnum + cnum}')
    if vitoria == True:
        print('Você venceu! Vamos jogar novamente.')
        print('-' * 35)
    if vitoria == False:
        print(f'Você perdeu! Seu total de vitórias consecutivas foi {totv}.')
        break