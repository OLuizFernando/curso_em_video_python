matriz = [[], [], []]
for c in range(0, 3):
    matriz[0].append(int(input(f'Digite um número para [0, {c}]: ')))
for c in range(0, 3):
    matriz[1].append(int(input(f'Digite um número para [1, {c}]: ')))
for c in range(0, 3):
    matriz[2].append(int(input(f'Digite um número para [2, {c}]: ')))
print('-' * 32)
print(f'[ {matriz[0][0]:^3} ][ {matriz[0][1]:^3} ][ {matriz[0][2]:^3} ]')
print(f'[ {matriz[1][0]:^3} ][ {matriz[1][1]:^3} ][ {matriz[1][2]:^3} ]')
print(f'[ {matriz[2][0]:^3} ][ {matriz[2][1]:^3} ][ {matriz[2][2]:^3} ]')