n1 = input("Digite o primeiro número: ")
n2 = input("Digite o segundo número: ")
n3 = input("Digite o terceiro número: ")
# Calculando menor valor digitado: (Por padrão, coloquei o A já sendo o de menor valor)
menor = n1
if n2 <= n1 and n3:
    menor = n2
if n3 <= n1 and n3:
    menor = n3
print(f'O menor número digitado foi {menor}')

# Calculando maior valor digitado: (Por padrão, coloquei o A já sendo o de maior valor)
maior = n1
if n2 > n1 and n3:
    maior = n2
if n3 > n1 and n2:
    maior = n3
print(f'O maior número digitado foi {maior}')

if n1 == n2 == n3:
    print("Porém, os valores digitados são idênticos!")
