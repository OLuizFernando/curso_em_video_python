n1 = int(input('Digite o 1° número inteiro: '))
n2 = int(input('Digite o 2° número inteiro: '))
if n1 > n2:
    print(f'{n1} é o número MAIOR.')
elif n2 > n1:
    print(f'{n2} é o número MAIOR.')
elif n1 == n2:
    print('Não existe número maior.')