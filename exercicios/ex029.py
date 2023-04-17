vel = float(input('Digite a velocidade do carro: '))
multa = (vel - 80) * 7
if vel > 80.0:
    print('A velocidade máxima permitida é de 80.0Km/h.\nVocê foi multado no valor de R${}'.format(multa))
else:
    print('Você está dentro da velocidade permitida.')