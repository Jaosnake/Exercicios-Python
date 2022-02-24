n = 1
m = 1
i = 0
calculo = 0
soma = []
soma_final = 0
termos = int(input('Digite o número de termos que quer calcular: '))
print ('S = ',end ='')
while i <= termos:
    print (f'{n+i}/{m+i} + ', end='')
    i+=1
    m+=1
    calculo = (n+i) / (m+i)
    soma.append(calculo)
    soma_final = sum(soma)
print ('... + n/m')
print (f'\nSoma da série = {soma_final:.2f}')
