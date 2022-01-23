x = int(input("Digite o ano para verificar se ele é bissexto: "))
bissexto = (x % 4)
if bissexto == 0:
    print("O ano digitado é bissexto")
else:
    print("O ano digitado NÃO é bissexto")
print("Fim do aplicativo")
