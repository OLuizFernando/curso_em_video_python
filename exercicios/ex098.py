def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-' * 40)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            cont -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 40)
print('Personalize sua contagem.')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo : '))
contador(ini, fim, pas)