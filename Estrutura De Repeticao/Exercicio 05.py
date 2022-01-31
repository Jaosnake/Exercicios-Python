n1 = str(input('Digite o nome da primeira cidade: '))
n2 = str(input('Digite o nome da segunda cidade: '))
cidadeA = float (input(f'Insira a população atual de {n1}: '))
cidadeB = float (input(f'Insira a população atual de {n2}: '))
taxa = float (input(f'Digite em % taxa anual de crescimento populacional de {n1}: '))
taxa2 = float (input(f'Digite em % taxa anual de crescimento populacional de {n2}: '))
anos = 0


while cidadeA <= cidadeB:
    cidadeA = cidadeA + ((cidadeA * taxa)/100)
    cidadeB = cidadeB + ((cidadeB * taxa2)/100)
    anos+=1
print (f'Demorará {anos} anos para a população das 2 cidades se igualarem')