times = ('América-MG', 'Athletico-PR', 'Atlético-MG', 'Bahia', 'Botafogo',
         'Corinthians', 'Coritiba', 'Cruzeiro', 'Cuiabá', 'Flamengo',
         'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional',
         'Palmeiras', 'Bragantino', 'Santos', 'São Paulo', 'Vasco da Gama')
print(f'Times do Brasileirão: {times}')
print(f'5 primeiros: {times[0:5]}')
print(f'Zona de rebaixamento: {times[-4:]}')
print(f'Lista em ordem alfabética: {sorted(times)}')
print(f'O Corinthians se encontra na posição: {times.index("Corinthians") + 1}')
