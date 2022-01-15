peso = float(input('Quantos KG de peixe o João Papo-de-Pescador trouxe?: '))
taramax = 50
excesso = peso - 50
multa = excesso * 4

print(f'João Papo-de-Pescador trouxe {peso}KG de peixe, ultrapassou {excesso}KG e vai pagar uma multa de R$ {multa:.2f}')
