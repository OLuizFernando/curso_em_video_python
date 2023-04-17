lista = []
cont = 1
resp = ''
while True:
    lista.append(int(input(f'Digite o {cont}° número: ')))
    cont += 1
    resp = str(input('Quer continuar? [S/N] ')).strip().lower()
    if resp[0] == 'n':
        break
print(f'Você digitou {len(lista)} números.')
print(f'Ordem decrescente da lista: {sorted(lista, reverse=True)}')
if lista.count(5) == 0:
    print('Número 5 não encontrado na lista.')
else:
    print('Número 5 encontrado na lista.')