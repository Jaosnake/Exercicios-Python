
while True:
    maior = menor = count = 0
    soma = 0
    while True:
        temp = float(input('Digite a temperatura para cálculo. Digite 0 para sair: '))
        count+=1
        if temp == 0:
            count-=1
            break
        else:
            if temp > maior:
                maior = temp
            else:
                menor = temp
        soma +=temp
    print (f'\nNúmero de temperaturas inseridas no sistema: {count}')
    print (f'Temperaturas -- Maior: {maior}°C / Menor: {menor}°C')
    print (f'Média = {soma/count}°C')
    opcao = int (input('\nDeseja refazer as medições? [1]-Sim / [2]-Não: '))
    if opcao == 1:
        continue
    else:
        print ('Saindo do programa.')
        break