x = int(input('Digite um número para saber se ele é número primo: '))
total = 0
for i in range(1, x + 1):
    if x % i == 0:
        total += 1
print (f'O número {x} foi divisível {total} vezes.')
if not total > 2:
    print ('É um número primo')
else:
    print ('Não é um número primo')