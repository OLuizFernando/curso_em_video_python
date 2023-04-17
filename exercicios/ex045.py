from time import sleep
from random import randint
print('1 - 👊\n2 - ✋\n3 - ✌️')
player = int(input('Pedra, papel ou tesoura? '))
if player < 1 or player > 3:
    print('\033[0;31mERRO:\033[m Valor inválido digitado.')
else:
    cpu = randint(1, 3)
    print('JO...')
    sleep(0.5)
    print('KEN...')
    sleep(0.5)
    print('PÔ')
    if player == 1 and cpu == 1:
        print('👊 VS 👊')
        print('\033[0;33mEMPATE\033[m')
    elif player == 1 and cpu == 2:
        print('👊 VS ✋')
        print('\033[0;31mDERROTA\033[m')
    elif player == 1 and cpu == 3:
        print('👊 VS ✌️')
        print('\033[0;32mVITÓRIA\033[m')
    elif player == 2 and cpu == 1:
        print('✋ VS 👊')
        print('\033[0;32mVITÓRIA\033[m')
    elif player == 2 and cpu == 2:
        print('✋ VS ✋')
        print('\033[0;33mEMPATE\033[m')
    elif player == 2 and cpu == 3:
        print('✋ VS ✌️')
        print('\033[0;31mDERROTA\033[m')
    elif player == 3 and cpu == 1:
        print('✌️ VS 👊')
        print('\033[0;31mDERROTA\033[m')
    elif player == 3 and cpu == 2:
        print('✌️ VS ✋')
        print('\033[0;32mVITÓRIA\033[m')
    elif player == 3 and cpu == 3:
        print('✌️ VS ✌️')
        print('\033[0;33mEMPATE\033[m')