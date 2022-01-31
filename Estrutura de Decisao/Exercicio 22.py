num = float(input('Digite um número para saber se ele é par ou ímpar: '))
teste = num % 2
if teste == 0:
    print (f'O número {num} é Par')
else:
    print (f'O número {num} é Ímpar')