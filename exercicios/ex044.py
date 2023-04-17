preco = float(input('Digite o preço do produto: R$'))
print('\033[0;34m1 -\033[m À VISTA NO PIX')
print('\033[0;34m2 -\033[m 1X NO CRÉDITO')
print('\033[0;34m3 -\033[m 2X NO CRÉDITO')
print('\033[0;34m4 -\033[m 3X OU MAIS NO CRÉDITO')
pag = str(input('Forma de pagamento: '))
if pag == '1':
    novopreco = preco - preco * (10 / 100)
    print('\033[0;37mR${:.2f}\033[m com 10% OFF: \033[0;32mR${:.2f}\033[m'.format(preco, novopreco))
elif pag == '2':
    novopreco = preco - preco * (5 / 100)
    print('\033[0;37mR${:.2f}\033[m com 5% OFF: \033[0;32mR${:.2f}\033[m'.format(preco, novopreco))
elif pag == '3':
    print('\033[0;37mR${:.2f}\033[m\n2X de \033[0;32mR${:.2f}\033[m'.format(preco, preco / 2))
elif pag == '4':
    vezes = int(input('Quantidade de parcelas: '))
    novopreco = preco + preco * (20 / 100)
    print('\033[0;37mR${:.2f}\033[m\n{}X de \033[0;32mR${:.2f}\033[m \033[0;37mcom juros\033[m'.format(preco, vezes, novopreco / vezes))
else:
    print('\033[0;31mERRO:\033[m Forma de pagamento inválida.')