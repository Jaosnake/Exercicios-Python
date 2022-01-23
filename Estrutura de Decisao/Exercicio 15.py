x = float (input('Digite o valor da primeira reta do triangulo: '))
y = float (input('Digite o valor da segunda reta do triangulo: '))
z = float (input('Digite Digite o valor da terceira reta triangulo: '))

if x <= y + z and y <= z + x and z <= x + y:
    print ('Os valores digitados formam um triângulo.')
    if x == y == z:
        print ('Triângulo Equilátero')
    elif x != y != z != x:
        print ('Triângulo Escaleno')
    else:
        print ('Triangulo Isósceles')
else:
    print ('Os valores digitados NÃO formam um triângulo. ')