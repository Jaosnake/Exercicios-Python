n = int(input('Digite um número: '))
print(f'\nNúmeros primos entre 1 e {n}: ')
x = 2
while x <= n - 1:
    a = 0
    b = 1
    while b < 100:
        if x % b == 0:
            a += 1
        b += 1
    if a == 2:
        print(x, end=' ')
    x += 1