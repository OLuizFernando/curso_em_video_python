from modulos import ex107
from modulos import ex108
p = float(input('Digite o preço: R$ '))
print(f'Metade de {ex108.moeda(p)} ------------> {ex108.moeda(ex107.metade(p))}')
print(f'Dobro de {ex108.moeda(p)} -------------> {ex108.moeda(ex107.dobro(p))}')
print(f'{ex108.moeda(p)} com 10% de aumento ---> {ex108.moeda(ex107.aumentar(p, 10))}')
print(f'{ex108.moeda(p)} com 13% de desconto --> {ex108.moeda(ex107.diminuir(p, 13))}')