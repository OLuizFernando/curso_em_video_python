from modulos import ex107
p = float(input('Digite o preço: R$ '))
print(f'Metade de R$ {p:.2f} ------------> R$ {ex107.metade(p):.2f}')
print(f'Dobro de R$ {p:.2f} -------------> R$ {ex107.dobro(p):.2f}')
print(f'R$ {p:.2f} com 10% de aumento ---> R$ {ex107.aumentar(p, 10):.2f}')
print(f'R$ {p:.2f} com 13% de desconto --> R$ {ex107.diminuir(p, 13):.2f}')