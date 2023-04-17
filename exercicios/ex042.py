l1 = float(input('Informe em centímetros o comprimento da 1° reta: '))
l2 = float(input('Informe em centímetros o comprimento da 2° reta: '))
l3 = float(input('Informe em centímetros o comprimento da 3° reta: '))
if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l1 + l2):
    print(f'As retas {l1}cm, {l2}cm e {l3}cm PODEM formar um triângulo.')
    if l1 == l2 == l3:
        print('O triângulo seria EQUILÁTERO.')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('O triângulo seria ISÓSCELES.')
    elif l1 != l2 != l3:
        print('O triângulo seria ESCALENO.')
else:
    print(f'As retas {l1}cm, {l2}cm e {l3}cm NÃO podem formar um triângulo.')