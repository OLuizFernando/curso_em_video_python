matriz = [[], [], []]
seglinha = []
somapares = 0
for c in range(0, 3):
    matriz[0].append(int(input(f'Digite um número para [0, {c}]: ')))
for c in range(0, 3):
    matriz[1].append(int(input(f'Digite um número para [1, {c}]: ')))
for c in range(0, 3):
    matriz[2].append(int(input(f'Digite um número para [2, {c}]: ')))
print('-' * 32)
print(f'[ {matriz[0][0]} ][ {matriz[0][1]} ][ {matriz[0][2]} ]')
print(f'[ {matriz[1][0]} ][ {matriz[1][1]} ][ {matriz[1][2]} ]')
print(f'[ {matriz[2][0]} ][ {matriz[2][1]} ][ {matriz[2][2]} ]')
print('-' * 32)
for c in range(0, 3):
    if matriz[0][c] % 2 == 0:
        somapares += matriz[0][c]
for c in range(0, 3):
    if matriz[1][c] % 2 == 0:
        somapares += matriz[1][c]
for c in range(0, 3):
    if matriz[2][c] % 2 == 0:
        somapares += matriz[2][c]
for c in range(0, 3):
    seglinha.append(matriz[1][c])
print(f'Soma dos números pares: {somapares}')
print(f'Soma dos números da terceira coluna: {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'Maior número da segunda linha: {max(seglinha)}')