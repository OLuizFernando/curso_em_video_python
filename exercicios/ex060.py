from math import factorial
num = int(input('Digite um número: '))
fat = num
print(f'{num}! = ', end='')
while num > 0:
    if num == 1:
        print(f'{num} =', end=' ')
        num -= 1
    else:
        print(f'{num} x', end=' ')
        num -= 1
print(factorial(fat))