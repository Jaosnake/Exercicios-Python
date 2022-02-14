num = 1
um_quarto = dois_quartos = tres_quartos = quatro_quartos = count = 0
while num >= 0:
    num = int(input('Digite qualquer número inteiro positivo: '))
    print('Digite um número negativo para parar')
    count+=1
    if 0 <= num <= 25:
        um_quarto+=1
    elif 26 <= num <= 50:
        dois_quartos +=1
    elif 51 <= num <= 75:
        tres_quartos+=1
    elif 76 <= num <= 100:
        quatro_quartos+=1
    else:
        print ('Pronto! Calculando...')
        count-=1

print (f'Foram contabilizados {count} números')
print (f'Há {um_quarto} números entre 0-25')
print (f'Há {dois_quartos} números entre 26-50')
print (f'Há {tres_quartos} números entre 51-75')
print (f'Há {quatro_quartos} números entre 76-100')
