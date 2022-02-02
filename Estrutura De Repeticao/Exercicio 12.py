num = int(input('Digite um número para saber sua tabuada: '))
count = 0
print ('=' * 15)
for i in range(1, 11):
    count+=1
    print (f'{num} x {i} = {num * i}')
print ('=' * 15)