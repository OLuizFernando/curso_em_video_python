sal = float(input('Digite seu salário: '))
aum1 = sal + (sal * (10 / 100))
aum2 = sal + (sal * (15 / 100))
if sal > 1250:
    print('Com 10% de aumento, você receberia: R${:.2f}'.format(aum1))
else:
    print('Com 15% de aumento, você receberia: R${:.2f}'.format(aum2))