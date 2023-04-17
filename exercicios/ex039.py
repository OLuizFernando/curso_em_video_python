from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
if idade < 18:
    print(f'Fique tranquilo, você só terá que se alistar daqui {18 - idade} ano(s).')
elif idade == 18:
    print('Já está na hora de você se alistar.')
elif idade > 18:
    r = str(input('Você já se alistou? [S/N] '))
    if r.upper() in 'S SIM SS YES':
        print('Que bom! Você já fez sua obrigação com o Estado, pode ficar tranquilo.')
    elif r.upper() in 'N NÃO NÂO NAO NN NO':
        print(f'Já passou da hora de se alistar! Você está {idade - 18} ano(s) atrasado.')