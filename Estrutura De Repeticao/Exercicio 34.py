num = int(input('Valor de N para cálculo de número primo: '))
count = 0
div = []
for i in range(1,num+1):
    if num % i == 0:
        count += 1
if count == 2:
    print(f'O número {num} é primo')
else:
   print(f'O número {num} não é primo')