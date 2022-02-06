c1 = c2 = c3 = 0
eleitores = int(input ('Digite o número de eleitores: '))
print('Escolha para qual candidato o voto será computado: ')
print('Candidato n° 1 = Digite 1')
print('Candidato n° 2 = Digite 2')
print('Candidato n° 2 = Digite 3')
for i in range (1, eleitores):
    voto = int(input(f'Digite o voto do {i}° eleitor: '))
    if voto == 1:
        c1+=1
    elif voto == 2:
        c2+=1
    elif voto == 3:
        c3+=1
print ('Resultado da Votação: ')
print (f'Candidato n° 1 - Votos = {c1}')
print (f'Candidato n° 1 - Votos = {c2}')
print (f'Candidato n° 1 - Votos = {c3}')