litros = float(input('Digite a quantidade de litros abastecida: '))
print ('Digite o tipo de combustível abastecido: ')
tipo = str (input('[A] - álcool -- [G] - gasolina: ')).upper().split()[0]
gas = litros * 2.50
alcool = litros * 1.90

if litros <= 20 and tipo in 'Aa':
    valorfinal = alcool - (alcool * 0.03)
    print ('=*'*17)
    print (f'Abastecimento até 20L de Álcool, desconto de 3%')
    print (f'Você economizou R$ {alcool - valorfinal:.2f}')
    print (f'Total a pagar : R$ {valorfinal:.2f}')
    print ('=*'*17)
elif litros > 20 and tipo in 'Aa':
    valorfinal = alcool - (alcool * 0.05)
    print ('=*' * 17)
    print (f'Abastecimento acima de 20L de Álcool, desconto de 5%')
    print (f'Você economizou R$ {alcool - valorfinal:.2f}')
    print (f'Valor Final : {valorfinal:.2f}')
    print ('=*' * 17)

if litros <= 20 and tipo in 'Gg':
    valorfinal = gas - (gas * 0.04)
    print ('=*' * 17)
    print (f'Abastecimento acima de 20L de Gasolina, desconto de 4%')
    print (f'Você economizou R$ {gas - valorfinal:.2f}')
    print (f'Valor Final : {valorfinal:.2f}')
    print ('=*' * 17)
elif litros > 20 and tipo in 'Gg':
    valorfinal = gas - (gas * 0.06)
    print ('=*' * 17)
    print (f'Abastecimento acima de 20L de Gasolina, desconto de 6%')
    print (f'Você economizou R$ {gas - valorfinal:.2f}')
    print (f'Valor Final : {valorfinal:.2f}')
    print ('=*' * 17)