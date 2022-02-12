divida = float(input("Digite o valor da divida: "))
parcela = 1
juros = 0
print("Valor da divida: ", end="  ")
print("Valor do juros: ", end="  ")
print("Quantidade de parcelas: ", end="  ")
print("Valor da parcela: ")

for i in range(5):
    if parcela == 1:
        juros = 1
        v_juros = 0
    elif parcela == 4:
        parcela = 3
        juros = 1.10
    elif parcela == 6 or parcela == 7:
        parcela = 6
        juros = 1.15
    elif parcela == 9 or parcela == 10:
        parcela = 9
        juros = 1.20
    elif parcela == 12 or parcela == 13:
        parcela = 12
        juros = 1.25

    v_juros = divida * (juros - 1)
    divida_com_juros = divida * juros
    valor_parcela = divida_com_juros / parcela

    print(f'R$ {divida_com_juros:.2f}', end='                 ')
    print(f'{v_juros:.2f}', end='                 ')
    print(f'{parcela:.2f}', end='                      ')
    print(f'R$ {valor_parcela:.2f}')
    parcela += 3