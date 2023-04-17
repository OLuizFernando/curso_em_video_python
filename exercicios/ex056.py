media = 0
maisvelho = 0
nomemaisvelho = ''
totsub20 = 0
for c in range(1, 5):
    if c < 5:
        print(f'========== {c}° PESSOA ==========')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    media = media + idade
    if c == 1 and sexo.upper() == 'M':
        maisvelho = idade
        nomemaisvelho = nome
    else:
        if idade > maisvelho and sexo.upper() == 'M':
            maisvelho = idade
            nomemaisvelho = nome.title()
    if sexo.upper() == 'F' and idade < 20:
        totsub20 = totsub20 + 1
print(f'Média de idade: {media / 4}')
print(f'{nomemaisvelho} é o homem mais velho, com {maisvelho} anos.')
print(f'Total de mulheres com menos de 20 anos: {totsub20}')
