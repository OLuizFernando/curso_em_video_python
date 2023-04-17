maior = 0
menor = 0
for c in range(1, 6):
    kg = float(input(f'Digite o peso da {c}° pessoa (Kg): '))
    if c == 1:
        maior = kg
        menor = kg
    else:
        if kg > maior:
            maior = kg
        if kg < menor:
            menor = kg
print(f'Maior peso: {maior}Kg')
print(f'Menor peso: {menor}Kg')