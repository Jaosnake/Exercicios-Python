cds = int(input('Digite a quantidade de CDs adquiridos: '))
total = 0
for i in range (1, cds):
    valor = float(input(f'Digite o valor do {i}° CD: '))
    total+=valor
print (f'Número de CDs adquiridos: {cds}')
print (f'Valor total gasto: {total}')
print (f'Média de R$ gasto: {total/cds}')