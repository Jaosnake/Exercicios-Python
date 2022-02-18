aluno = 1
pior_aluno = 10
melhor_aluno = maior_acerto = media_notas = escolha = 0
menor_acerto = 10
gabarito = []
while True:
    certa = errada = 0
    print ('Escolha a opção desejada: ')
    print ('[A] - Aluno')
    print ('[P] - Professor')
    escolha = str(input('Opção: ')).upper()
    if escolha.isdigit() or escolha != 'AaPp':
        print ('\nDigite a letra A para ALUNO ou P para PROFESSOR')
        if escolha in 'Aa':
            if len(gabarito) == 0:
                print ('Não é possível começar a prova sem o gabarito.\n')
            else:
                for i in range(1,11):
                    print (f'Digite a resposta da {i}° pergunta: ')
                    resposta = str(input('Resposta: ')).upper()
                    if i == 1 and resposta in gabarito[0]:
                        certa+=1
                    if i == 2 and resposta in gabarito[1]:
                        certa+=1
                    if i == 3 and resposta in gabarito[2]:
                        certa+=1
                    if i == 4 and resposta in gabarito[3]:
                        certa+=1
                    if i == 5 and resposta in gabarito[4]:
                        certa+=1
                    if i == 6 and resposta in gabarito[5]:
                        certa +=1
                    if i == 7 and resposta in gabarito[6]:
                        certa +=1
                    if i == 8 and resposta in gabarito[7]:
                        certa+=1
                    if i == 9 and resposta in gabarito[8]:
                        certa+=1
                    if i == 10 and resposta in gabarito[9]:
                        certa+=1
                    if certa > maior_acerto:
                        maior_acerto = certa
                        melhor_aluno = aluno
                    if certa < maior_acerto:
                        menor_acerto = certa
                        pior_aluno = aluno
                media_notas+=certa
                print (f'10 perguntas, {certa} respostas corretas.')
                continuar = str(input('Deseja continuar? [S]im ou [N]ão: ')).strip()[0].upper()
                aluno += 1
                if continuar in 'Ss':
                    continue
                else:
                    aluno-=1
                    break
        elif escolha in 'Pp':
            gabarito.clear()
            for i in range(1, 11):
                lista = str(input(f'Insira a resposta correta para a pergunta número {i}: ')).upper()
                gabarito.append(lista)
            print ('\nOk Professor. A lista de respostas corretas ficou assim: ')
            print (gabarito)

print(f'Número de alunos que utilizaram o sistema: {aluno}')
print(f'Aluno com mais acertos: {maior_acerto} respostas (aluno {melhor_aluno})')
print(f'Aluno com menos acertos: {menor_acerto} respostas (aluno {pior_aluno})')
print(f'A média de acerto dos alunos foram {int(media_notas/aluno)} respostas corretas')