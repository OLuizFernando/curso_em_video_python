lista = []
for c in range(0, 5):
    num = (int(input(f'Digite o {c + 1}° valor: ')))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado no fim da lista.')
    else:
        for c in range(0, len(lista)):
            if num <= lista[c]:
                lista.insert(c, num)
                print(f'Adicionado na posição {c}')
                break
print(lista)