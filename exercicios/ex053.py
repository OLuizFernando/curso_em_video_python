frase = str(input('Digite uma frase ou palavra: ')).strip().replace(' ', '')
frase_inv = frase[::-1]
print(f'O inverso de {frase} é {frase_inv}.')
if frase == frase_inv:
    print(f'{frase} é um PALÍNDROMO.')
else:
    print(f'{frase} NÃO é um palíndromo.')