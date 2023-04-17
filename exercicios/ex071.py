valor = int(input('Valor de saque: R$'))
nota50 = valor // 50
nota20 = (valor - nota50 * 50) // 20
nota10 = (valor - (nota50 * 50) - (nota20 * 20)) // 10
nota01 = (valor - (nota50 * 50) - (nota20 * 20) - (nota10 * 10))
if nota50 > 0:
    print(f'{nota50} nota(s) de R$ 50.00')
if nota20 > 0:
    print(f'{nota20} nota(s) de R$ 20.00')
if nota10 > 0:
    print(f'{nota10} nota(s) de R$ 10.00')
if nota01 > 0:
    print(f'{nota01} nota(s) de R$ 1.00')