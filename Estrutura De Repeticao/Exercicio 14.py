impar = 0
par = 0

for i in range (1,11):
    num = int(input(f'Digite o {i}° número: '))
    if num %2 !=0:
        impar+=1
    else:
        par+=1
print (f'Quantidade de números pares: {par}')
print (f'Quantidade de números ímpares: {impar}')