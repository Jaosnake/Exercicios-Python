print('=+' * 19)
print('Exercício 03 - Estrutura de Repetição')
print('=+' * 19)

nome = str(input('Digite o nome: ')).strip()
idade = int(input('Digite a idade: '))
salario = float(input('Digite o salário: R$ '))
sexo = str(input('[M/F]: ')).strip().upper()[0]
civil = str(input('Estado Civil: [S]olteiro - [C]asado - [V]iúvo - [D]ivorciado: ')).upper().strip()[0]

while len(nome) <= 3:
    print('Nome inválido!')
    nome = str(input('Insira o nome (maior que 3 letras): '))
while idade < 0 or idade > 150:
    print('Idade inválida!')
    idade = int(input('Digite a idade (Entre 0 e 150 anos): '))
while salario <= 0:
    print('Salário inválido!')
    salario = float(input('Digite o salário (Valor maior que 0): '))
while sexo != 'M' and sexo != 'F':
    print('Opção Inválida!')
    sexo = str(input('Escolha sexo entre [M/F]: ')).strip().upper()
while civil != 'S' and civil != 'C' and civil != 'V' and civil != 'D':
    print('Estado Civil inserido com caracteres inválidos!')
    civil = str(input('Escolha o estado civil: [S]olteiro - [C]asado - [V]iúvo - [D]ivorciado: ')).upper().strip()[0]
print("Todas as opções foram inseridas corretamente. Fim do programa.")
