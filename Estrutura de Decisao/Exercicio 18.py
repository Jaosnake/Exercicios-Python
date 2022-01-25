dia = int (input('Digite o dia: '))
mes = str (input('Digite o mes: '))
ano = int (input('Digite o ano: '))

if dia < 0 or dia > 31:
    print ('Dia Inválido!')
elif mes < '0' and mes > '12':
    print ('Mês Inválido!')
elif ano < 0:
    print ('Ano inválido!')

if mes in '01,03,05,07,08,10,12':
    ultimo_dia = 31
elif mes in '02':
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        ultimo_dia = 29
    else:
        ultimo_dia = 28
else:
    ultimo_dia = 30
print (f'{dia}/{mes}/{ano} são datas válidas.')
print (f'Dia {ultimo_dia} é ultimo dia do mês dos dados conferidos.')
