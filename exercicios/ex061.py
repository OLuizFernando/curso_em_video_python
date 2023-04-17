n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
termo = n
cont = 1
while cont <= 10:
    print(f'{termo} → ', end='')
    termo += r
    cont += 1
print('FIM')