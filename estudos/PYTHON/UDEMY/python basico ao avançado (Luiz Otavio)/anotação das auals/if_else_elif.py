n1 = input("Digite um numero inteiro: ")
if n1.isdigit():
    n1 = int(n1)
    if n1 % 2 == 0 :
        print("O valor que você digitou foi par.")
    elif n1 % 2 == 1:
        print("O valor é impar.")
else:
    print("Valor invalido.")

n2 = input("Digite a hora em inteiro :")
if n2.isdigit():
    n2 = int(n2)
    if n2 > 0  and n2 < 11 :
        print("Bom Dia")
    elif n2 > 12 and n2 < 17 :
        print("Boa tarde")
    else:
        print("Boa Noite")
else:
    print("Valor invalido !!!")

nome =input("Qual o seu nome :")
quant_caracter =  len(nome)

if quant_caracter <= 4 :
    print("Nome Curto ")
elif quant_caracter <= 6 :
    print("Seu nome é normal")
else :
    print("Seu nome é grande ")