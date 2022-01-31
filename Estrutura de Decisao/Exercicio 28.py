print ('Promoção de Carnes ')
print ('1 - Filé Duplo ')
print ('2 - Alcatra')
print ('3 - Picanha')
opcao = int(input('Escolha a opção desejada = '))
kg = float(input('Digite a quantidade em KG: '))
print('Cartão Tabajara? (5% Desconto)')
cartao = int(input('[1] - Sim / [2] - Não = '))

if opcao == 1:
    carne = 'Filé Duplo'
    if kg <= 5:
        preco = kg * 4.90
    else:
        preco = kg * 5.80

if opcao == 2:
    carne = 'Alcatra'
    if kg <= 5:
        preco = kg * 5.90
    else:
        preco = kg * 6.80

if opcao == 3:
    carne = 'Picanha'
    if kg <= 5:
        preco = kg * 6.90
    else:
        preco = kg * 7.80

if cartao == 1:
    cctabajara = 'Sim'

    desconto = preco - (preco * 0.05)
    total = desconto
else:
    cctabajara = 'Não'
    total = preco

print ('=*'*10,'Supermercados Tabajara','=*'*10)
print (f'Tipo de Carne                      {carne}')
print (f'Quantidade(KG)                     {kg}')
print (f'Preço Total                     R$ {preco:.2f}')
print (f'Cartão Tabajara                    {cctabajara}')
print (f'Total c\ Desconto               R$ {total:.2f}')