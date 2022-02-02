n = int(input('Digite o número de valores que quer calcular: '))
soma = menor = maior = contador = 0

for i in range (1, n+1):
    v = int(input(f'Digite o {i}° valor: '))
    soma +=v
    contador+=1
    if contador == 1:
        maior = menor = v
    else:
        if v > maior:
            maior = v
        if v < menor:
            menor = v
print (f'A soma dos itens é igual a = {soma}')
print (f'O menor dos valores é = {menor}')
print (f'O maior dos valores é = {maior}')
