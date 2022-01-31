num = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
soma=0
for i in range (num,num2+1):
   soma = i+soma
print (f'A soma dos valores de {num} a {num2} é de {soma}')
