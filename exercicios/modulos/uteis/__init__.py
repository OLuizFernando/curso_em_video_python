def leiaint(msg):
    while True:
        n = str(input(msg)).strip().replace(' ', '')
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('\033[31mERRO: Digite um NÚMERO INTEIRO.\033[m')
    return valor


def leiafloat(msg):
    while True:
        n = str(input(msg)).strip().replace(' ', '')
        if n.replace('.', '').replace(',', '').isnumeric():
            valor = float(n)
            break
        else:
            print('\033[31mERRO: Digite um NÚMERO REAL.\033[m')
    return valor


def leiadinheiro(msg):
    while True:
        r = str(input(msg)).strip()
        if r.replace(' ', '').replace(',', '').replace('.', '').isnumeric():
            r = float(r.replace(' ', '').replace(',', '.'))
            break
        else:
            print(f'\033[31mERRO: "{r}" não é um valor válido.\033[m')
    return r


def dinheio(v):
    r = str(f'R$ {v:.2f}').replace('.', ',')
    return r