from random import randint
from operator import itemgetter
jogadas = {'player 1': randint(1, 6), 'player 2': randint(1, 6), 'player 3': randint(1, 6), 'player 4': randint(1, 6)}
rank = []
for k, v in jogadas.items():
    print(f'{k} tirou o número {v}')
rank = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print('-' * 25)
for i, v in enumerate(rank):
    print(f'{i + 1}° Lugar: {v[0]} com {v[1]}')