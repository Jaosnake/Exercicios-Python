letra = str(input('Digite uma letra: ')).upper().split()[0]
if letra.isnumeric():
    print ('Somente será aceito no campo LETRAS')
elif letra in 'AEIOU':
    print(f'A letra {letra[0]} é uma vogal.')
else:
    print(f'A letra {letra[0]} é uma consoante.')
