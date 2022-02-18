cod = 1
cc = bauru = bauru_ovo = hamburguer = cheese = refri = 0
total_cc = total_bauru = total_bauru_ovo = total_hamburguer = total_cheese = total_refri = 0

while True:
    if cod == 0:
        break
    print('Digite 0 para finalizar o pedido')
    cod = int(input('Insira o código: '))
    if cod == 100:
        cc = int(input('Digite a quantidade de Cachorro Quente: '))
        total_cc = cc * 1.20
    elif cod == 101:
        bauru = int(input('Digite a quantidade de Bauru Simples: '))
        total_bauru = bauru * 1.30
    elif cod == 102:
        bauru_ovo = int(input('Digite a quantidade de Bauru com Ovo: '))
        total_bauru_ovo = bauru_ovo * 1.50
    elif cod == 103:
        hamburguer = int(input('Digite a quantidade de Hambúrguer: '))
        total_hamburguer = hamburguer * 1.20
    elif cod == 104:
        cheese = int(input('Digite a quantidade de Cheeseburguer: '))
        total_cheese = cheese * 1.30
    elif cod == 105:
        refri = int(input('Digite a quantidade de Refrigerante: '))
        total_refri = refri * 1.00
    elif cod == 0:
        print('Código para finalização do pedido foi digitado\n')
    else:
        print('Código inválido!')

print('Especificação', end='      ')
print('Código', end='        ')
print('Preço', end='      \n')
print (f'Cachorro Quente      100        R$ {total_cc:.2f}', end='\n')
print (f'Bauru Simples        101        R$ {total_bauru:.2f}', end='\n')
print (f'Bauru com Ovo        102        R$ {total_bauru_ovo:.2f}', end='\n')
print (f'Hambúrguer           103        R$ {total_hamburguer:.2f}', end='\n')
print (f'Cheeseburguer        104        R$ {total_cheese:.2f}',end='\n')
print (f'Refrigerante         105        R$ {total_refri:.2f}',end='\n')
print (f'Total                -->        R$ {total_cc+total_bauru+total_bauru_ovo+total_cheese+total_hamburguer+total_refri:.2f}')