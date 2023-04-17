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