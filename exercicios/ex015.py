dia = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foram percorridos com o carro? '))
preco = (dia * 60) + (km * 0.15)
print('O preço total do aluguel foi de R${:.2f}'.format(preco))