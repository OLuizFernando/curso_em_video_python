n = int(input('Digite um número: '))
f1 = 0
f2 = 1
print(f'{f1} → {f2}', end='')
cont = 3
while cont <= n:
    f3 = f1 + f2
    print(f' → {f3}', end='')
    f1 = f2
    f2 = f3
    cont += 1
print(' → FIM')