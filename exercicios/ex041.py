from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
if idade <= 9:
    print('Você é considerado MIRIM.')
elif idade <= 14:
    print('Você é considerado INFANTIL.')
elif idade <= 19:
    print('Você é considerado JÚNIOR.')
elif idade <= 24:
    print('Você é considerado SÊNIOR.')
elif idade > 24:
    print('Você é considerado MASTER.')