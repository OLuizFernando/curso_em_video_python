nome0 = str(input('Digite seu nome completo: '))
nome = nome0.strip().split()
print('Primeiro nome:', nome[0].capitalize())
print('Último nome:', nome[len(nome) - 1].capitalize()) 