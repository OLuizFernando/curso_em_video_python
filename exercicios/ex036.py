casa = float(input('Digite o valor do imóvel: R$'))
salario = float(input('Digite o seu salário: R$'))
ano = int(input('Digite em quantos anos deseja parcelar: '))
parcela = casa / (ano * 12)
if parcela >= salario * (30 / 100):
    print('NEGADO: As parcelas da casa não podem exceder 30% do seu salário.')
else:
    print('Pagando em {}x, as parcelas ficarão RS{:.2f} / mês.'.format((ano * 12), parcela))