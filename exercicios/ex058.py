from random import randint
from time import sleep
num = randint(0, 10)
chute = int(input('Pensei em num número entre 0 e 10.\nTente adivinhar: '))
certo = False
c = 1
while certo == False:
    if chute > 10 or chute < 0:
        chute = int(input('Valor inválido. Chute um número entre 0 e 10.\nTente adivinhar: '))
    elif chute != num:
        chute = int(input('Errou! Tente novamente: '))
        c += 1
    elif chute == num:
        certo = True
print(f'Acertou! Pensei no número {num}.\nVocê teve que tentar {c} vezes para acertar.')