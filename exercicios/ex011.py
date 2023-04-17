comp = float(input('Digite o comprimento da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))
area = comp * alt
l = area / 2
print('A área da parede é de {}m².'.format(area))
print('Para pintá-la, precisaria de {}L de tinta.'.format(l))