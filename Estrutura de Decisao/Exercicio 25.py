sus = 0
op1 = str(input("Telefonou para a vítima?: ")).strip()[0].upper()
op2 = str(input("Esteve no local do crime?: ")).strip()[0].upper()
op3 = str(input("Mora perto da vítima?: ")).strip()[0].upper()
op4 = str(input("Devia para a vítima?: ")).strip()[0].upper()
op5 = str(input("Já trabalhou com a vítima?: ")).strip()[0].upper()

if op1 in 'Ss':
    sus+=1
if op2 in 'Ss':
    sus+=1
if op3 in 'Ss':
    sus+=1
if op4 in 'Ss':
    sus+=1
if op5 in 'Ss':
    sus+=1

print ('\nPelas afirmações acima, o veredito é:')
if sus == 2:
    print ('Suspeito')
elif sus == 3 or sus == 4:
    print ('Cúmplice')
elif sus == 5:
    print ('Culpado(a)')
else:
    print ('Inocente')
