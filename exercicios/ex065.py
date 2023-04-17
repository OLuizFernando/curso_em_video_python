resp = 's'
maior = menor = cont = soma = 0
while resp.lower() in 's sim ss':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    resp = str(input('Quer continuar? [S/N] '))
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print(f'Total de números digitados: {cont}')
print(f'Média: {media}')
print(f'Soma de todos: {soma}')
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')