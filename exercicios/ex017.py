from math import sqrt
catop = float(input('Informe o comprimento do cateto oposto: '))
catad = float(input('Informe o comprimento do cateto adjacente: '))
qhip = (catop**2) + (catad**2)
hip = sqrt(qhip)
print('A hipotenusa deste triângulo é igual à: {}'.format(hip))