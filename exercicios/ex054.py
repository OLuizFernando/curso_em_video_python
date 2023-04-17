from datetime import datetime
tmen = 0
tmai = 0
for c in range(1, 8):
    n = int(input(f'Digite o ano de nascimento da {c}° pessoa: '))
    if (datetime.today().year - 18) >= n:
        tmai += 1
    else:
        tmen += 1
print(f'Total de maiores de idade: {tmai}')
print(f'Total de menores de idade: {tmen}')