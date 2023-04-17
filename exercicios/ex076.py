pc = ('Intel Core i5 10400F', 699.99,
      'GeForce GTX 1050 2GB', 706.25,
      'RAM 16GB 2666Mhz DDR4', 429.99,
      'Gigabyte H410M H V3', 579.99,
      'HD Seagate 1TB SATA', 279.99,
      '500w Pcyes 80 Plus', 437.82,)
total = 0
print('-' * 40)
print(f"{'CARRINHO DE COMPRAS':^40}")
print('-' * 40)
for c in range(0, len(pc), 2):
      total += pc[c + 1]
      print(f'{pc[c]:.<30}R$ {pc[c + 1]:>.2f}')
print('-' * 40)
print(f'{"TOTAL":.<29}R$ {total:.2f}')