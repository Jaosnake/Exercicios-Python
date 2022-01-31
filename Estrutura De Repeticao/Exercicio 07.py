maior = 0
for i in range (1,6):
    num = int(input(f'Insira o {i}° número: '))
    if num > maior:
        maior = num
print (f'O maior número dos digitados é o {maior}')