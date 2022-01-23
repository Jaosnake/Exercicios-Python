print('Cálculo de Salário')
vr = float(input('Digite o valor da hora trabalhada: '))
ht = float(input('Digite o número de horas trabalhadas: '))

mes = vr * ht

if mes <= 900:
    print(f' Salário Bruto: ({vr} * {ht}):  R$ {mes:.2f}')
    print(f' (-) IR - ISENTO ')
    print(f' (-) INSS(10 %):                R$ {mes * 0.10:.2f}')
    print(f' FGTS (11 %):                   R$ {mes * 0.11:.2f}')
    print(f' Sindicato (3%):                R$ {mes * 0.03:.2f}')
    print(f' Total de descontos:            R$ {mes * 0.13:.2f}')
    print(f' Salário Liquido:               R$ {mes - (mes * 0.13):.2f}')

elif mes > 900 and mes <= 1500:
    print(f' Salário Bruto: ({vr} * {ht}):  R$ {mes:.2f}')
    print(f' (-) IR(5 %):                   R$ {mes * 0.05:.2f}')
    print(f' (-) INSS(10 %):                R$ {mes * 0.10:.2f}')
    print(f' FGTS (11 %):                   R$ {mes * 0.11:.2f}')
    print(f' Sindicato (3%):                R$ {mes * 0.03:.2f}')
    print(f' Total de descontos:            R$ {mes * 0.18:.2f}')
    print(f' Salário Liquido:               R$ {mes - (mes * 0.18):.2f}')

elif mes > 1500 and mes <= 2500:
    print(f' Salário Bruto: ({vr} * {ht}):   R$ {mes:.2f}')
    print(f' (-) IR(10 %):                   R$ {mes * 0.10:.2f}')
    print(f' (-) INSS(10 %):                 R$ {mes * 0.10:.2f}')
    print(f' FGTS (11 %):                    R$ {mes * 0.11:.2f}')
    print(f' Sindicato (3%):                 R$ {mes * 0.03:.2f}')
    print(f' Total de descontos:             R$ {mes * 0.23:.2f}')
    print(f' Salário Liquido:                R$ {mes - (mes * 0.23):.2f}')
else:
    print(f' Salário Bruto: ({vr} * {ht}):  R$ {mes:.2f}')
    print(f' (-) IR(20 %):                   R$ {mes * 0.20:.2f}')
    print(f' (-) INSS(10 %):                 R$ {mes * 0.10:.2f}')
    print(f' FGTS (11 %):                    R$ {mes * 0.11:.2f}')
    print(f' Sindicato (3%):                 R$ {mes * 0.03:.2f}')
    print(f' Total de descontos:             R$ {mes * 0.33:.2f}')
    print(f' Salário Liquido:                R$ {mes - (mes * 0.33):.2f}')
