num = int(input('Digite um número inteiro: '))
print('Escolha a \033[0;37mbase de conversão\033[m:')
print('Digite 1 para \033[0;34mbinário\033[m')
print('Digite 2 para \033[0;34moctal\033[m')
print('Digite 3 para \033[0;34mhexadecimal\033[m')
base = int(input())
if base < 1 or base > 3:
    print('\033[0;31mERRO: O número digitado não corresponde à nenhuma base de conversão.\033[m')
elif base == 1:
    print('A forma \033[0;37mbinária\033[m de {} é: {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('A forma \033[0;37moctal\033[m de {} é: {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('A forma \033[0;37mhexadecimal\033[m de {} é: {}'.format(num, hex(num)[2:]))
