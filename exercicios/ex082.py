lista = []
pares = []
impares = []
cont = 1
while True:
    lista.append(int(input(f'Digite o {cont}° número: ')))
    cont += 1
    resp = str(input('Quer continuar? [S/N] ')).strip().lower()
    if resp[0] == 'n':
        break
for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f'Números digitados: {lista}')
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')