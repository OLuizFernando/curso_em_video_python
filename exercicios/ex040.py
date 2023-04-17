n1 = float(input('Digite sua 1° nota: '))
n2 = float(input('Digite sua 2° nota: '))
n3 = float(input('Digite sua 3° nota: '))
n4 = float(input('Digite sua 4° nota: '))
media = (n1 + n2 + n3 + n4) / 4
print('Sua média foi: {:.1f}'.format(media))
if media < 5:
    print('Status do aluno: \033[0;31mREPROVADO\033[m')
elif media >= 5 and media < 6:
    print('Status do aluno: \033[0;33mRECUPERAÇÃO\033[m')
elif media >= 6:
    print('Status do aluno: \033[0;32mAPROVADO\033[m')