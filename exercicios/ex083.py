exp = str(input('Digite uma expressão: '))
lista = []
for carac in exp:
    if carac == '(':
        lista.append('(')
    elif carac == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressão correta.')
else:
    print('Expressão incorreta.')