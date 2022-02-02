print('=*' * 15)
print('Sequência de Fibonacci')
print('=*' * 15)
sequencia = int(input('Digite um número para calcular a Sequência de Fibonacci: '))
t1 = 1
t2 = 1
print(f'{t1} -> {t2}', end='')
count = 3
while count <= sequencia:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    count += 1
print(" -> Fim")
