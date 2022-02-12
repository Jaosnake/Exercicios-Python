maior_aluno = 0
menor_aluno = 0
maior_altura = 0
menor_altura = 300
for i in range (1,10):
    aluno = int(input('Aluno n°: '))
    altura = float(input('Altura(cm): '))
    if altura > maior_altura:
        maior_aluno = aluno
        maior_altura = altura
    if altura < menor_altura:
        menor_aluno = aluno
        menor_altura = altura
    print (f'Maior aluno : {maior_aluno}')
    print (f'Menor aluno : {menor_aluno}')
    print (f'Maior altura : {maior_altura}cm')
    print (f'Menor altura : {menor_altura}cm')
