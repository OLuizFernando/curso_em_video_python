from random import randint
from time import sleep
num = randint(0, 5)
chute = int(input('Pensei em um número entre 0 e 5, tente adivinhar: '))
if chute > 5 or chute < 0:
    print('Valor inválido. Chute um número entre 1 e 5.')
else:
    print('Processando...')
    sleep(1)
    if chute == num:
      print('Parabéns! Você acertou.')
    else:
       print('Infelizmente, você errou! Pensei no número {}'.format(num))