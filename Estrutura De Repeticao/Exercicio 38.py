salario = int(input('Digite o salário de 1995: R$ '))
ano = 1995
while ano <= 2021:
    salario *= 1.015
    ano += 1
print(f'Salário do ano {ano} = R$ {salario:.2f}')