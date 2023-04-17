lista = []
for c in range(1, 6):
    lista.append(int(input(f'Digite o {c}° número: ')))
print('Você digitou os números: ', end='')
for num in lista:
    print(num, end=' ')
print(f'\nMaior número: {max(lista)}, na posição {lista.index(max(lista)) + 1}')
print(f'Menor número: {min(lista)}, na posição {lista.index(min(lista)) + 1}')
