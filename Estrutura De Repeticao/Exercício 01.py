print('=+' * 19)
print('Exercício 01 - Estrutura de Repetição')
print('=+' * 19)
x = 0
while 0 <= x <= 10:
    x = float(input('Digite uma nota de 0 a 10: '))
    if x < 0 or x > 10:
        print('Valor inválido!')
        x = float(input('Digite uma nota de 0 a 10: '))
