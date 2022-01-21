n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2

if media < 7:
    print(f'{media} de média. Reprovado.')
elif media >= 7 and media < 10:
    print(f'{media} de média. Aprovado.')
elif media == 10:
    print('Aluno foi Aprovado com Distinção.')
