turmas = int(input('Digite o número de turmas: '))
total = 0
for i in range (1,turmas):
    alunos = int(input('Digite o número de alunos de cada turma: '))
    if alunos > 40:
        print ('Não pode haver mais de 40 alunos na turma.')
        break
    else:
        total+=alunos
print (f'Total de alunos: {total}')
print (f'Média total de alunos: {(total/turmas)}')