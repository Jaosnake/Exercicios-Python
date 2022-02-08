p_maior = 0 #todos têm peso maior que 0 kg.
p_menor = 500 #todos terão de ter peso menor que 500 kg.
a_maior = 0 #todos têm altura maior que 0 cm.
a_menor = 300 #altura de referência máxima é 300 cm.
cod_maior_altura = cod_menor_altura = 0
cod_maior_peso = cod_menor_peso = 0
soma_peso = soma_altura = 0
c_altura = c_peso = 0 #divisor do peso/altura
while True:
    print ('Digite 0 para parar o programa\n')
    cod = int(input('Digite o código do cliente: '))
    if cod == 0:
        break
    altura = float(input(f'Digite a altura do cliente (cm): '))
    peso = float(input(f'Digite o peso do cliente (KG): '))
    soma_peso += peso
    soma_altura += altura
    c_peso += 1
    c_altura += 1
    if altura > a_maior:
        a_maior = altura
        cod_maior_altura = cod
    if altura < a_menor:
        a_menor = altura
        cod_menor_altura = cod
    if peso > p_maior:
        p_maior = peso
        cod_maior_peso = cod
    if peso < p_menor:
        p_menor = peso
        cod_menor_peso = cod
    print(f'\nCódigo do Maior peso: {cod_maior_peso}')
    print(f'Código do Menor peso: {cod_menor_peso}')
    print(f'Maior peso: {p_maior}KG')
    print(f'Menor peso: {p_menor}KG')
    print(f'Média peso: {soma_peso / c_peso:.2f}KG\n')
    print(f'Código da Maior altura: {cod_maior_altura}')
    print(f'Código da Menor altura: {cod_menor_altura}')
    print(f'Maior altura: {a_maior}cm')
    print(f'Menor altura: {a_menor}cm')
    print(f'Média altura: {soma_altura / c_altura:.2f}cm\n')
