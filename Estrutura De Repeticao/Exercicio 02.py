print('=+' * 19)
print('Exercício 02 - Estrutura de Repetição')
print('=+' * 19)

user = str(input('Digite o nome do usuário: ')).strip()
senha = str(input('Digite a sua senha (Não será aceito o nome como parte da senha): ')).strip()

while user != senha:
    user = str(input('Digite o nome do usuário: ')).strip()
    senha = str(input('Digite a sua senha (Não será aceito o nome como parte da senha): ')).strip()
    if user == senha:
        print(f'Não será aceito o nome como parte da senha! {user} - {senha}')
