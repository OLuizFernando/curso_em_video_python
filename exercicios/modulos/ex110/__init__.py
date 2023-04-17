def resumo(v, a, d):
    def moeda(x):
        r = str(f'R$ {x:.2f}').replace('.', ',')
        return r
    print('-' * 35)
    print(f'{"RESUMO DO VALOR":^35}')
    print('-' * 35)
    print(f'{"Preço analisado:":<25}{moeda(v):<}')
    print(f'{"Metade do preço:":<25}{moeda(v / 2):<}')
    print(f'{"Dobro do preço:":<25}{moeda(v * 2):<}')
    print(f'{a}{"% de aumento:":<23}{moeda(v + (v * (a / 100))):<}')
    print(f'{d}{"% de desconto:":<23}{moeda(v - (v * (d / 100))):<}')