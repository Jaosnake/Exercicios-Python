notas = soma = 0
n = int(input('Digite quantas notas quer calcular: '))

for i in range (1, n+1):
    notas = int(input(f'Digite o valor da {i}° nota: '))
    soma+=notas
print (f'Número de notas digitadas: {n}')
print (f'Média dos valores digitados: {soma/n}')