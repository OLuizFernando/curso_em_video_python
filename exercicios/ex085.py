lista = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c}° número: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print(f'Números PARES: {sorted(lista[0])}')
print(f'Números ÍMPARES: {sorted(lista[1])}')