numeral = int(input('Digite o número: '))
if numeral < 0 or numeral > 1000:
    print ('Só serão aceitos valores entre 1 - 1000')
else:
    #unidade
    uni = numeral % 10
    #unidade - numero
    numeral = (numeral - uni)/10
    #dezena
    dez = numeral % 10
    #dezena - numero
    numeral = (numeral - dez)/10
    #centena
    cent = numeral
    #transformando em inteiros
    dez = int(dez)
    cent = int(cent)

print (f'{cent} centenas, {dez} dezenas, {uni} unidades')