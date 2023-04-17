dist = float(input('Qual será a distância percorrida em Km? '))
preco1 = dist * 0.50
preco2 = dist * 0.45
if dist < 1:
    print('Distância inválida. Realizamos apenas viagens de no mínimo 1.0Km')
else:
    if dist <= 200:
        print('Para uma viagem de {}Km, o preço da passagem será: R${:.2f}'.format(dist, preco1))
    else:
        print('Para uma viagem de {}Km, o preço da passagem será: R${:.2f}'.format(dist, preco2))