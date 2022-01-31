num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
print ('=*'*15)
print ("Qual operação entre os números acima deseja realizar?")
print ('Soma            [1]')
print ('Subtração       [2]')
print ('Multiplicação   [3] ')
print ('Divisão         [4]')
opcao = int (input('Escolha a opção desejada: '))
print ('=*'*15)

if opcao == 1:
    soma = num1+num2
    print (f'A soma dos 2 valores: {soma}')
    if soma % 1 == 0:
        print(f'{soma} é Inteiro')
    else:
        print(f'{soma} é Decimal')
    if soma % 2 == 0:
        print (f'{soma} é Par')
    else:
        print (f'{soma} é Ímpar')
    if soma > 0:
        print (f'{soma} é Positivo')
    else:
        print (f'{soma} é Negativo')

elif opcao == 2:
    sub = num1-num2
    print (f'A subtração dos 2 valores: {sub}')
    if sub % 1 == 0:
        print(f'{sub} é Inteiro')
    else:
        print(f'{sub} é Decimal')
    if sub % 2 == 0:
        print (f'{sub} é Par')
    else:
        print (f'{sub} é Ímpar')
    if sub > 0:
        print (f'{sub} é Positivo')
    else:
        print (f'{sub} é Negativo')

elif opcao == 3:
    multi = num1*num2
    print (f'A multiplicação dos 2 valores: {multi}')
    if multi % 1 == 0:
        print(f'{multi} é Inteiro')
    else:
        print(f'{multi} é Decimal')
    if multi % 2 == 0:
        print (f'{multi} é Par')
    else:
        print (f'{multi} é Ímpar')
    if multi > 0:
        print (f'{multi} é Positivo')
    else:
        print (f'{multi} é Negativo')

elif opcao == 4:
    div = num1/num2
    print (f'A divisão dos 2 valores: {div}')
    if div % 1 == 0:
        print(f'{div} é Inteiro')
    else:
        print(f'{div} é Decimal')
    if div % 2 == 0:
        print (f'{div} é Par')
    else:
        print (f'{div} é Ímpar')
    if div > 0:
        print (f'{div} é Positivo')
    else:
        print (f'{div} é Negativo')
else:
    print ('Opção Inválida')