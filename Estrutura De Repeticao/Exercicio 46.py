import math
tentativa = ('Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto')
nome = ''
saltos_realizados = []
media = count = 0

while True:
    nome = str(input('Digite o nome do Atleta (Digite SAIR para finalizar o programa): '))
    if nome in 'SAIRsair':
        print ('Saindo do programa')
        break
    else:
       for i in range (0,5):
        saltos = float(input(f'Digite o valor do {tentativa[i]} salto (em Metros): '))
        saltos_realizados.append(saltos)
    maior = max(saltos_realizados)
    menor = min(saltos_realizados)
    print (f'\nAtleta: {nome}\n')
    for count in range (0,5):
        print (f'{tentativa[count]} salto = {saltos_realizados[count]} m')
        count+=1
    print (f'\nMelhor salto = {maior} m')
    print (f'Pior salto = {menor} m')
    saltos_realizados.remove(maior)
    saltos_realizados.remove(menor)
    media = (math.fsum(saltos_realizados)/3)
    print (f'Média dos demais saltos = {media:.1f} m')
    print (f'\nResultado final: ')
    print (f'{nome}: {media:.1f} m')
    saltos_realizados.clear()