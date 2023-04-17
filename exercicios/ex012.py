preco = float(input('Digite o preço original do produto: R$'))
desc = preco - (preco * 0.05)
print('Com 5% de desconto, o produto ficará RS${:.2f}'.format(desc))