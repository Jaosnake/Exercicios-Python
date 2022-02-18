import math
tentativa = ('Primeira', 'Segunda', 'Terceira', 'Quarta', 'Quinta', 'Sexta', 'Sétima')
nome = ''
notas_totais = []
media = 0
count = 0

while True:
    nome = str(input('Digite o nome do Atleta (Digite SAIR para finalizar o programa): '))
    if nome in 'SAIRsair':
        print ('Saindo do programa')
        break
    else:
       for i in range (0,7):
        notas = float(input(f'Digite a {tentativa[i]} nota: '))
        notas_totais.append(notas)
    maior = max(notas_totais)
    menor = min(notas_totais)
    print(f'\nAtleta: {nome}\n')
    for count in range (0,7):
        print (f'nota: {notas_totais[count]}')
        count+=1
    print (f'\nResultado final: ')
    print (f'Atleta: {nome}')
    print(f'Melhor nota: {maior}')
    print(f'Pior nota: {menor}')
    notas_totais.remove(maior)
    notas_totais.remove(menor)
    media = (math.fsum(notas_totais) / 5)
    print(f'Média: {media:.2f}')
    notas_totais.clear()