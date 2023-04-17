def moeda(v):
    r = str(f'R$ {v:.2f}').replace('.', ',')
    return r


def aumentar(v, p, f=False):
    r = v + (v * (p / 100))
    if f:
        r = moeda(r)
    return r


def diminuir(v, p, f=False):
    r = v - (v * (p / 100))
    if f:
        r = moeda(r)
    return r


def dobro(v, f=False):
    r = v * 2
    if f:
        r = moeda(r)
    return r


def metade(v, f=False):
    r = v / 2
    if f:
        r = moeda(r)
    return r


def resumo(v, a, d):
    print('-' * 35)
    print(f'{"RESUMO DO VALOR":^35}')
    print('-' * 35)
    print(f'{"Preço analisado:":<25}{moeda(v):<}')
    print(f'{"Metade do preço:":<25}{moeda(v / 2):<}')
    print(f'{"Dobro do preço:":<25}{moeda(v * 2):<}')
    print(f'{a}{"% de aumento:":<23}{moeda(v + (v * (a / 100))):<}')
    print(f'{d}{"% de desconto:":<23}{moeda(v - (v * (d / 100))):<}')