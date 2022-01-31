cidadeA = 8000
cidadeB = 20000
taxa = 0.03
taxa2 = 0.015
anos = 0


while cidadeA <= cidadeB:
    cidadeA = cidadeA + (cidadeA * taxa)
    cidadeB = cidadeB + (cidadeB * taxa2)
    anos+=1
print (f'Cidade A: {cidadeA:.0f}')
print (f'Cidade B: {cidadeB:.0f}')
print (f'Demorará {anos} anos para a população das 2 cidades se igualarem')
