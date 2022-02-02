f = 1
count = 1
fatorial = int(input('Digite o número para saber seu fatorial: '))
for i in range (1,fatorial+1):
    f*=i
    count -=1
print(f'Fatorial de {fatorial}! = {f}')
