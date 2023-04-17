n1 = int(input('Digite o 1° número inteiro: '))
n2 = int(input('Digite o 2° número inteiro: '))
print('\033[34m[1]\033[m somar\n\033[34m[2]\033[m multiplicar\n\033[34m[3]\033[m maior\n\033[34m[4]\033[m novos números\n\033[34m[5]\033[m sair do programa')
r = int(input(''))
while r != 5:
    if r > 5 or r < 1:
        r = int(input('\033[31mERRO:\033[m Valor inválido.\nDigite uma das opções acima: '))
    elif r == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
        print('\033[34m[1]\033[m somar\n\033[34m[2]\033[m multiplicar\n\033[34m[3]\033[m maior\n\033[34m[4]\033[m novos números\n\033[34m[5]\033[m sair do programa')
        r = int(input(''))
    elif r == 2:
        print(f'{n1} X {n2} = {n1 * n2}')
        print('\033[34m[1]\033[m somar\n\033[34m[2]\033[m multiplicar\n\033[34m[3]\033[m maior\n\033[34m[4]\033[m novos números\n\033[34m[5]\033[m sair do programa')
        r = int(input(''))
    elif r == 3:
        if n1 > n2:
            print(f'{n1} > {n2}')
            print('\033[34m[1]\033[m somar\n\033[34m[2]\033[m multiplicar\n\033[34m[3]\033[m maior\n\033[34m[4]\033[m novos números\n\033[34m[5]\033[m sair do programa')
            r = int(input(''))
        elif n2 > n1:
            print(f'{n2} > {n1}')
            print('\033[34m[1]\033[m somar\n\033[34m[2]\033[m multiplicar\n\033[34m[3]\033[m maior\n\033[34m[4]\033[m novos números\n\033[34m[5]\033[m sair do programa')
            r = int(input(''))
        elif n1 == n2:
            print(f'{n1} = {n2}')
            print('\033[34m[1]\033[m somar\n\033[34m[2]\033[m multiplicar\n\033[34m[3]\033[m maior\n\033[34m[4]\033[m novos números\n\033[34m[5]\033[m sair do programa')
            r = int(input(''))
    elif r == 4:
        n1 = int(input('Digite o 1° número inteiro: '))
        n2 = int(input('Digite o 2° número inteiro: '))
        print('\033[34m[1]\033[m somar\n\033[34m[2]\033[m multiplicar\n\033[34m[3]\033[m maior\n\033[34m[4]\033[m novos números\n\033[34m[5]\033[m sair do programa')
        r = int(input(''))
print('\033[33mPrograma finalizado.\033[m')