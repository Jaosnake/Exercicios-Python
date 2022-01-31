maior = 0
count = 0
for i in range (1,6):
    num = int(input(f'Insira o {i}° número: '))
    count +=num
    if num > maior:
        maior = num
print (f'O maior número dos digitados é o {maior}.')
print (f'A soma entre si dos valores digitados é {count}.')
print (f'A média dos números digitados é {count/5} ')