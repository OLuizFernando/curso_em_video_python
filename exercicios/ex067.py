while True:
    n = int(input('Digite um número: '))
    print('-' * 20)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:02} = {n * c:02}')
    print('-' * 20)