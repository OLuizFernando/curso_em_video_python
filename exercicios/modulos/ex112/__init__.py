def leiadinheiro(msg):
    while True:
        r = str(input(msg)).strip()
        if r.replace(' ', '').replace(',', '').replace('.', '').isnumeric():
            r = float(r.replace(' ', '').replace(',', '.'))
            break
        else:
            print(f'\033[31mERRO: "{r}" não é um preço válido.\033[m')
    return r