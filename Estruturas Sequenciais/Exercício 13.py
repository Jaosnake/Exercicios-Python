alt = float(input('Digite a altura do paciente (em Metros): '))

masc = (72.7 * alt) - 58
fem = (62.1 * alt) - 44.7
print(f'O peso ideal do paciente,se masculino, é de {masc:.2f}KG')
print(f'O peso ideal do paciente,se feminino, é de {fem:.2f}KG')

# É uma estrutura simples. Se fosse com Decisões (IF/ELSE)
# sexo = '' >>>> Esse parâmetro vai lá no cabeçalho da estrutura
# sexo = str(input('[M/F]: ')).upper().strip()[0]
# if sexo in 'Mm':
#    print(f'O peso ideal do paciente, masculino, é de {masc:.2f}KG')
# else:
#    print(f'O peso ideal do paciente, feminino, é de {fem:.2f}KG')
