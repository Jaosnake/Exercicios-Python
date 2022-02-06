n = int(input('Fatorial de: '))
c = n
f = 1
print (n,'= ',end='')
while c > 0:
    print(f'{c}',end=' ')
    if c > 1:
        print('.',end=' ')
    else:
        print(' = ',end=' ')
    f *= c
    c -= 1
print(f'{f}')