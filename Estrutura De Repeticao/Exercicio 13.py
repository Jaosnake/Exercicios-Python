b= int(input('Digite o numero base: '))
e= int(input('Digite o expoente: '))
base = 1
count = 0

for i in range (e):
   base=base*b
   count=count+1

print (f'Base {b} ^ Expoente {e} = {base}')
