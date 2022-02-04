x = int(input('Digite um número para saber se ele é número primo: '))
total = 0
div = []
ndiv = []
for i in range(1, x + 1):
    if x % i == 0:
        total += 1
        ndiv.append(i)
    else:
        div.append(i)
if x == 1:
    print (f'O número um (1) não é considerado um número primo, porque ele é divisível apenas por ele mesmo.')
elif total == 2:
    print (f'É um número primo, pois ele é divisível por = {ndiv}.')
else:
    print (f"Não é um número primo, pois ele é divisível por {total} números com resto 0: {ndiv}")