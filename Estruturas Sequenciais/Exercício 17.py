# 10% de margem de segurança já calculado na linha LITRO com 0.1 multiplicando
metros = float(input('Digite a área a ser pintada em m2: '))
litro = metros / 6 * 0.10
lata = litro / 18
galao = litro / 3.6
precogalao = 0
preco = 0

if lata % 18 != 0:
    lata = lata + 1
    preco = lata * 80

if galao % 3.6 != 0:
    galao = galao + 1
    precogalao = galao * 25

# Misturar latas e galões na mesma conta
mlata = int(litro / 18.0)
mgalao = int((litro - (mlata * 18)) / 3.6)

if litro - (mlata * 18) % 3.6 != 0:
    mgalao += 1

print(f'Para pintar {metros}m2, irá utilizar {litro:.2f}l de tinta')
print(f'São necessários {lata:.2f} latas de tinta de 18l no valor de R$ {preco:.2f}')
print(f'São necessários {galao:.2f} galão de tinta de 3.6l no valor de R$ {precogalao:.2f}')
print(f'Mistura: {mlata} latas e {mgalao} galões = R$ {(mlata * 80) + (mgalao * 25)}')
