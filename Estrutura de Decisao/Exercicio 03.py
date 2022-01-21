sexo = str(input('[M/F]: ')).strip().upper()[0]
if sexo == "M":
    print(f'Sexo Masculino')
elif sexo == "F":
    print(f'Sexo Feminino')
else:
    print(f'Sexo inválido! Campo aceita somente [M/F]')
