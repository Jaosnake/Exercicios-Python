while True:
    count = 0
    valor = 1
    soma = 0
    print ('Lojas Tabajara')
    print ('Digite 0 quando quiser parar de registrar os produtos')
    while True:
        count+=1
        valor = float(input(f'Produto {count}: R$ '))
        soma+=valor
        if valor == 0:
            count-=1
            break
    print (f'Total = R$ {soma:.2f}')
    dinheiro = float(input('Valor pago em dinheiro: R$ '))
    print (f'Dinheiro: R$ {dinheiro:.2f}')
    if dinheiro < soma:
        print (f'O dinheiro recebido não paga a conta! Falta R$ {dinheiro-soma:.2f} para pagar os produtos')
    else:
        print (f'Troco: R$ {dinheiro - soma:.2f}')
    opcao = str(input('Deseja inserir outra compra? : ')).strip().upper()[0]
    if opcao in 'Ss':
        continue
    else:
        print ('Tenha um bom dia!')
        break
