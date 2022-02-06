print ('Panificadora Pão de Ontem - Tabela de preços ')
pao = float(input('Preço do pão: R$ '))
for i in range (1,51):
    print (f'{i} = R$ {i*pao:.2f}')
