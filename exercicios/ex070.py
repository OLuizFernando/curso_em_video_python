totalgasto = precomaisbarato = float(0)
totmaismil = cont = 0
nomemaisbarato = resp = ''
while True:
    cont += 1
    print(f'CADASTRE O {cont}° PRODUTO')
    print('-' * 22)
    nome = str(input('Produto: ')).strip().title()
    preco = float(input('Preço: R$'))
    totalgasto += preco
    if preco > 1000:
        totmaismil += 1
    if cont == 1:
        nomemaisbarato = nome
        precomaisbarato = preco
    else:
        if preco < precomaisbarato:
            nomemaisbarato = nome
            precomaisbarato = preco
    print()
    resp = str(input('Deseja coninuar? [S/N] ')).strip().lower()
    print()
    print('-' * 22)
    if resp[0] == 'n':
        break
print(f'Total gasto: R${totalgasto:.2f}')
print(f'Total de produtos acima de mil reais: {totmaismil}')
print(f'Produto mais barato: {nomemaisbarato}')