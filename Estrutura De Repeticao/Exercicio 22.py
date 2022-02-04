x = int(input('Digite um número para saber se ele é número primo: '))
total = 0
div = []
ndiv = []

for i in range(1, x + 1):
    if x % i == 0:
        total += 1
        ndiv.append(i)
    else:
        div.append(i+1)
if total == 2:
    print (f'É um número primo. Foi divisível por {ndiv}')
else:
    print (f'Não é um número primo, pois ele é divisível por {div}')
