p1 = float(input('Digite o valor do primeiro produto: R$ '))
p2 = float(input('Digite o valor do segundo produto: R$ '))
p3 = float(input('Digite o valor do terceiro produto: R$ '))


barato = p1
if p2 <= p1 and p3:
    barato = p2
if p3 <= p1 and p3:
    barato = p3
print(f'O valor do produto digitado mais barato foi R${barato:.2f}')

