import math

print('Insira os valores para calcular ax2 + bx + c')
a = int(input('Digite o valor de A: '))
if a == 0:
    print('Valor de A = 0. Não é uma equação de 2° grau. Finalizando programa')
else:
    b = int(input('Digite o valor de B: '))
    c = int(input('Digite o valor de C: '))
    delta = (b * b) - 4 * (a * c)
    d1 = (-b + math.sqrt(delta)) / (2 * a)
    d2 = (-b - math.sqrt(delta)) / (2 * a)
if delta < 0:
    print('Delta negativo. Programa Encerrado.')
elif delta == 0:
    print(f'A equação possui uma raiz real:\n Delta = {delta} raiz x1: {d1}')
else:
    print(f'A equação possui duas raízes reais: \nDelta = {delta} \nraiz x1: {d1} \nraiz x2: {d2} ')
