n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2

if media > 9 and media <= 10:
    print (f'{media} é a média do aluno')
    print ('Conceito A')
    print ('APROVADO')

if media > 7.5 and media <= 9:
    print(f'{media} é a média do aluno')
    print('Conceito B')
    print('APROVADO')

if media > 6 and media <= 7.5:
    print(f'{media} é a média do aluno')
    print('Conceito C')
    print('APROVADO')

if media > 4 and media <= 6:
    print(f'{media} é a média do aluno')
    print('Conceito D')
    print('REPROVADO')

if media > 0 and media <= 4:
    print(f'{media} é a média do aluno')
    print('Conceito E')
    print('REPROVADO')
