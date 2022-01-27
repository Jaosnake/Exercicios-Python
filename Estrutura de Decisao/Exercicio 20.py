n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
n3 = float(input('Digite a terceira nota do aluno: '))

media = (n1+n2+n3)/3

if 0 <= media < 7:
    print(f'Reprovado. Média {media:.2f}')
if 7 <= media < 10:
    print (f'Aprovado. Média {media:.2f}')
if media == 10:
    print(f'Aprovado com Distinção. Média {media:.2f}')