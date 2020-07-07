'''
#1
def sau(saudacao, nome):
    print(saudacao, nome)
    return
saudacao = input ("Qual nome da Saudação :")
nome = input("Qual o nome dele : ")
sau(saudacao,nome)

#2
def ler_numero(n1,n2,n3):
    h = print(n1+n2+n3)
    return h
n1 = int(input("Digite o primeiro numero "))
n2 = int(input("Digite o segundo numero "))
n3 = int(input("Digite o terceiro numero "))

def imposto (n1, n2):
    novo_valor = n1 + ((n2/100)*n1)
    return novo_valor

n1 = float(input("Qual o valor da mercadoria:"))
n2 = float(input("Qual o valor do imposto encima da mercadoria "))

resultado = imposto(n1,n2)

print(f'O valor da mercadoria é R$ {resultado}')

#duvida = se quando coloca variavel o loop do programa sobe pra função ,
#pq ele nao aceita varivel ?

'''
def fizz_bizz (n1):

    if n1 % 3 == 0 and n1 % 5 == 0 :
        var1 = print("FIZZZ BIZZZ")
        return var1
    elif n1 % 3 == 0 :
        var1 =print("FIZZZ")
        return var1
    elif n1 % 5 == 0 :
        var1 = print("BIZZ")
        return var1
    return  n1

n1 = float(input("Digite um valor : "))

resultado = fizz_bizz(n1)
