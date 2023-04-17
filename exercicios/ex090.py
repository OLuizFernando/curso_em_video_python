aluno = {}
aluno['NOME'] = str(input('Nome: ')).strip().title()
aluno['MÉDIA'] = float(input(f'Média de {aluno["NOME"]}: '))
if aluno['MÉDIA'] >= 6:
    aluno['SITUAÇÃO'] = 'Aprovado'
else:
    aluno['SITUAÇÃO'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual à {v}')