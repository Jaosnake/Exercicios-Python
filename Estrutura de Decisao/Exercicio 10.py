print ('Manhã = M')
print ('Vespertino = V')
print ('Noite = M')
turno = str(input('Digite o turno que você estuda: ')).strip().upper()[0]

if turno in 'Mm':
    print ('Bom dia!')
elif turno in 'Vv':
    print ('Boa tarde!')
elif turno in 'Nn':
    print ('Boa noite!')
else:
    print ('Valor inválido!')