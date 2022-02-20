termos = int(input('Digite o número de termos que quer calcular: '))
m = 1
i = 0
print ('S = 1 + ',end ='')
while i < termos:
    print (f'{1}/{m+i+1} + ', end='')
    i+=1
print ('... + 1/n')
