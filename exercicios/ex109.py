from modulos import ex109
p = float(input('Digite o preço: R$ '))
print(f'Metade de {ex109.moeda(p)} ------------> {ex109.metade(p, True)}')
print(f'Dobro de {ex109.moeda(p)} -------------> {ex109.dobro(p, True)}')
print(f'{ex109.moeda(p)} com 10% de aumento ---> {ex109.aumentar(p, 10, True)}')
print(f'{ex109.moeda(p)} com 13% de desconto --> {ex109.diminuir(p, 13, True)}')