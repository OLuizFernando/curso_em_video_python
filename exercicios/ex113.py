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


try:
    inteiro = leiaint('Digite um número INTEIRO: ')
except KeyboardInterrupt:
    print('\033[31mERRO: O usuário preferiu não informar o valor.\033[m')
    inteiro = '<null>'
try:
    real = leiafloat('Digite um número REAL: ')
except KeyboardInterrupt:
    print('\033[31mERRO: O usuário preferiu não informar o valor.\033[m')
    real = '<null>'
print(f'Número inteiro digitado: {inteiro}')
print(f'Número real digitado: {real}')