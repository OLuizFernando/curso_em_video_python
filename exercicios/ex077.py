tuple = ('DEPOIS', 'DE', 'PYTHON', 'VOU', 'APRENDER', 'JAVA')
for word in tuple:
    print(f'\nEm "{word}" temos ', end='')
    for letter in word:
        if letter.upper() in 'AÁÀÃÂÄEÉÈÊËIÍÌÎÏOÓÒÕÔÖUÚÙÛÜ':
            print(letter, end=' ')