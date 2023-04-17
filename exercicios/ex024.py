c = str(input('Digite o nome da sua cidade: '))
c1 = c.upper().strip().split()
print('Sua cidade começa com a palavra "Santo"?', 'SANTO' in c1[0])