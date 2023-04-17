def leiaint(msg):
    while True:
        n = str(input(msg)).strip().replace(' ', '')
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('\033[31mERRO: Valor inválido digitado.\033[m')
    return valor


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c} - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[33mSua Opção: \033[m')
    return opc