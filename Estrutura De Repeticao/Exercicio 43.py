cod = 1
count = cc = bauru = bauru_ovo = hamburguer = cheese = refri = 0
while True:
    if cod == 0:
        break
    print('Digite 0 para finalizar o pedido')
    cod = int(input('Insira o código: '))
    count+=1
    if cod == 100:
        cc+=1
    elif cod == 101:
        bauru+=1
    elif cod == 102:
        bauru_ovo+=1
    elif cod == 103:
        hamburguer+=1
    elif cod == 104:
        cheese+=1
    elif cod == 105:
        refri+=1
print('Especificação', end='      ')
print('Código', end='    ')
print('Preço', end='    ')