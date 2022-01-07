from math import pi
r = float(input('Digite o valor do raio do circulo para calcular a área: '))
a = pi*(r**2)
b = pi*(r**2)*100
print (f'O valor da área em metros: {a:.2f}m')
print (f'O valor da área em centímetros: {b:.2f}cm')