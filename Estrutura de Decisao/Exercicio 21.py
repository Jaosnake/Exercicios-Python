print ('=*'*20)
saque = int(input('Digite o valor que quer sacar: '))
if saque < 10 or saque > 600:
    print ('Só serão aceitos valores entre R$ 10 - R$ 600')
else:
   n100 = saque // 100
   n50 = (saque % 100) // 50
   n10 = (saque % 50) // 10
   n5 = (saque % 10) // 5
   n1 = (saque % 5) // 1

if n100 > 0:
    print (f'{n100} cédula(s) de R$ 100')
if n50 > 0:
    print (f'{n50} cédula(s) de R$ 50.00')
if n10 > 0:
    print (f'{n10} cédula(s) de R$ 10.00')
if n5 > 0:
    print (f'{n5} cédula(s) de R$ 5.00')
if n1 > 0:
    print (f'{n1} cédula(s) de R$ 1.00')
print ('=*'*20)