idade = total = 0
n = int(input('Digite o n° de pessoas que irão fazer parte do estudo: '))

for i in range (1, n+1):
    idade = int(input(f'Digite a idade do {i}° participante: '))
    total+=idade
media = total / n

if media <=25:
    print (f'\nMédia das idades: {media}. A turma é formada por pessoas jovens!')
elif media > 26 and media <= 60:
    print (f'\nMédia das idades: {media}. A turma é formada por pessoas adultas!')
elif media > 60:
    print(f'\nMédia das idades: {media}. A turma é formada por pessoas idosas!')


