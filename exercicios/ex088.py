from time import sleep
from random import randint
lista = []
quant = int(input('Número de jogos: '))
print('-' * 30)
print(f'{f"SORTEANDO {quant} JOGOS":^30}')
print('-' * 30)
for j in range(0, quant):
    for c in range(0, 6):
        while True:
            num = randint(1, 60)
            if num not in lista:
                lista.append(num)
                break
    sleep(0.5)
    print(f'{j + 1}° jogo: {lista[:]}')
    lista.clear()