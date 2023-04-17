n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{n} → ', end='')
        n += r
        cont += 1
    print('PAUSA')
    mais = int(input('Digite mais quantos termos você quer ver: '))
print('FIM')
print(f'A PA teve {total} termos no total.')