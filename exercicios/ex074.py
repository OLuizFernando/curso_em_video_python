from random import randint
num = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Números sorteados: {num[0]} {num[1]} {num[2]} {num[3]} {num[4]}')
print(f'Maior número: {max(num)}')
print(f'Menor número: {min(num)}')