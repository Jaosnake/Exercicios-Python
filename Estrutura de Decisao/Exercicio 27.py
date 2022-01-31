morango = float(input('Digite quantos KG de morango foram adquiridos: '))
maca = float(input('Digite quantos KG de maça foram adquiridos: '))

preco_morango = morango * 2.50
preco_morango5 = morango * 2.20
preco_maca = maca * 1.80
preco_maca5 = maca * 1.50

if morango <= 5:
    preco_final_morango = preco_morango
else:
    preco_final_morango = preco_morango5

if maca <=  5:
    preco_final_maca = preco_maca
else:
    preco_final_maca = preco_maca5
preco_final = preco_final_maca+preco_final_morango
print ('=*'*20)
if (maca+morango) > 8 or preco_final > 25.00:
    preco_final = preco_final - (preco_final * 0.10)
    if preco_final >25.00:
        print (f'Preço final dos produtos receberá um desconto de 10%')
    else:
        print (f'Peso final dos produtos dá direito a um desconto de 10%')
    print (f'Valor Morango (KG) = {preco_final_morango:.2f}')
    print (f'Valor Maça (KG) = {preco_final_maca:.2f}')
    print (f'Valor final = R$ {preco_final:.2f}')
    print('=*' * 20)
else:
    print(f'Valor Morango (KG) = {preco_final_morango:.2f}')
    print(f'Valor Maça (KG) = {preco_final_maca:.2f}')
    print(f'Valor final = R$ {preco_final:.2f}')
    print('=*' * 20)