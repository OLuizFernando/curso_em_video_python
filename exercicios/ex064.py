cont = 0
n = 0
soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        soma += n
        cont += 1
print(f'Você digitou {cont} números no total e a soma de todos é igual à {soma}.')