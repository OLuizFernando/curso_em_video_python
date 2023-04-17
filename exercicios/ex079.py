lista = []
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
    resp = str(input('Quer continuar? [S/N] ')).strip().lower()
    if resp[0] == 'n':
        break
print(sorted(lista))