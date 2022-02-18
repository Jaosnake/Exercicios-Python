nulo = branco = jose = joao = maria = ap = nulos_total = brancos_total = total_votos = 0
voto = 10
while True:
    if voto == 0:
        break
    print ('Eleicões 2022')
    print ('[1] José - [2] João - [3] Maria - [4] Aparecida', end='\n')
    print ('[5] Voto Nulo - [6] Voto em Branco', end='\n')
    voto = int(input('Digite o código do candidato: '))
    if voto == 1:
        jose+=1
    elif voto == 2:
        joao+=1
    elif voto == 3:
        maria+=1
    elif voto == 4:
        ap+=1
    elif voto == 5:
        nulo+=1
    elif voto == 6:
        branco+=1
    elif voto == 0:
        print('\nSerá iniciada a contagem de votos!')
    else:
        print ('Código inválido!')
total_votos = (jose+joao+maria+ap+nulo+branco)
nulos_total = ((nulo/total_votos)*100)
brancos_total = ((branco / total_votos)*100)
print (f'Total de Votos: {total_votos}')
print (f'[1] José - [2] João - [3] Maria - [4] Aparecida - [5] Voto Nulo - [6] Voto em Branco')
print (f' {jose}            {joao}            {maria}            {ap}           {nulo}               {branco}')
print (f'Total de Votos Nulos sobre total: {round(nulos_total)}%')
print (f'Total de Votos em Branco sobre total: {round(brancos_total)}%')