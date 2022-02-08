multi = int(input('Montar a tabuada de: '))
ini = int(input('Começa por: '))
fim = int(input('Termina em: '))
count=-1
print (f'\nVou montar a tabuada de {multi} começando em {ini} e terminando em {fim}: \n')

if fim < ini:
    print('Você digitou o número final menor que o inicial. Finalizando..')
else:
    for i in range (ini,fim+1):
        count+=1
        print (f'{multi} x {ini+count} = {multi*i}')