print('********* Reajuste Salarial, conforme regulamentação a seguir: *********')
print('Salários até R$ 280,00 : aumento de 20% ')
print('Salários entre R$ 280,00 e R$ 700,00 : aumento de 15% ')
print('Salários entre R$ 700,00 e R$ 1500,00 : aumento de 10% ')
print('Salários de R$ 1500,00 em diante : aumento de 5% ')
sal = float(input('\nDigite o salário do servidor para reajuste: R$ '))

if sal < 280:
    aum = sal * 0.20
    print(f'Salário antes do Reajuste: R${sal}')
    print(f'Faixa de aumento aplicado: 20%')
    print(f'Valor do aumento: RS {aum:.2f}')
    print(f'Salário final: R$ {sal + aum:.2f}')
elif sal >= 280 and sal < 700:
    aum = sal * 0.15
    print(f'Salário antes do Reajuste: R${sal}')
    print(f'Faixa de aumento aplicado: 15%')
    print(f'Valor do aumento: RS {aum:.2f}')
    print(f'Salário final: R$ {sal + aum:.2f}')
elif sal >= 700 and sal < 1500:
    aum = sal * 0.10
    print(f'Salário antes do Reajuste: R${sal}')
    print(f'Faixa de aumento aplicado: 10%')
    print(f'Valor do aumento: RS {aum:.2f}')
    print(f'Salário final: R$ {sal + aum:.2f}')
elif sal >= 1500:
    aum = sal * 0.05
    print (f'Salário antes do Reajuste: R${sal}')
    print (f'Faixa de aumento aplicado: 5%')
    print (f'Valor do aumento: RS {aum:.2f}')
    print(f'Salário final: R$ {sal + aum:.2f}')