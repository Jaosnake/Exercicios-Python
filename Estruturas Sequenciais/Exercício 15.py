hora = float (input('Valor da hora trabalhada: R$ '))
mes = float(input('Horas trabalhadas no mês: '))
bruto = hora*mes
ir = (bruto * 0.11)
inss = (bruto * 0.08)
sindicato = (bruto * 0.05)
descontos = (ir + inss + sindicato)
liquido = (bruto - descontos)
print(f'Salário bruto no mês => R$ {bruto:.2f}')
print(f'Desconto de IR => R$ {ir:.2f}')
print(f'Desconto de INSS => R$ {inss:.2f}')
print(f'Desconto de Sindicato => R$ {sindicato:.2f}')
print(f'Salário Líquido => R$ {liquido:.2f}')