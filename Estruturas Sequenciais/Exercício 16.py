metros = float(input('Digite a área a ser pintada em m2: '))
litro = metros / 3
tinta = metros / 54
custo = 80

print(f'Para pintar {metros} m2 de parede, são necessários {litro}L de tinta')
print(f'Quantidade de latas a serem compradas: {tinta:.2f}')
print(f'A lata custa R$ 80.00: Custo total: R$ {custo * tinta:.2f}')
