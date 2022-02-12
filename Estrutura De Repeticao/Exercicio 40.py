i_min = 0
i_max = 2000000
cod_min = 0
cod_max = 0
media_veiculos = 0
menor_2000 = 0
media_menor_2000 = 0
cidades = ['Primeira','Segunda','Terceira','Quarta','Quinta']

for i in range (1,6):
    cod = int(input(f'Digite o código da {cidades[i-1]} cidade: '))
    veiculos = int(input('Digite o n° de veículos de passeio registrados na cidade (em 1999): '))
    acidentes = int(input('Digite o n° de acidentes registrados com vítimas (em 1999): '))
    media_veiculos+=veiculos
    if veiculos <= 2000:
        menor_2000+=1
        media_menor_2000+=acidentes
    if acidentes > i_min:
        i_min = acidentes
        cod_min = cod
    if acidentes < i_max:
        i_max = acidentes
        cod_max = cod
print (f'Registro das 05 cidades efetuado com sucesso.\n')
print (f'Média de veículos registrados: {int(media_veiculos / 5)} veículos.')
print (f'Maior índice de acidentes é da cidade {cod_min} com {i_min} acidentes.')
print (f'Menor índice de acidentes é da cidade {cod_max} com {i_max} acidentes.')
print (f'Média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio: {int(media_menor_2000 / menor_2000)} acidentes')