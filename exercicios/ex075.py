tupla = (int(input('Digite o 1° número: ')),
         int(input('Digite o 2° número: ')),
         int(input('Digite o 3° número: ')),
         int(input('Digite o 4° número: ')))
print(f'Valores digitados: {tupla}')
print(f'O número 9 apareceu {tupla.count(9)} vezes')
if tupla.count(3) >= 1:
    print(f'O número 3 apareceu na {tupla.index(3) + 1}° posição')
else:
    print(f'O número 3 não foi encontrado')
print(f'Números Pares: ', end='')
for c in range(0, len(tupla)):
    if tupla[c] % 2 == 0:
        print(tupla[c], end=' ')