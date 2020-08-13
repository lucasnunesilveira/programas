"""
    -----------===-------------------Algoritumo de  pra fazer ----=============

    04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

    0   4   2   5   2   0   1   1   0   0   0   1 lista do cpf

    5   4   3   2   9   8   7   6   5   4   3   2 lista do multiplicar

    0   16  6   10  18  0   7   6   0   0   0   2  resultado da multiplição
    = 65
    Fórmula -> 11 - (65 % 11) = 1
    Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

    0   4   2   5   2   0   1   1   0   0   0   1   1   X
    6   5   4   3   2   9   8   7   6   5   4   3   2
    0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
    Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
    Segundo digito = 0

    Novo CNPJ + Digitos = 04.252.011/0001-10
    CNPJ Original =       04.252.011/0001-10
    Válido

    Recap.
    543298765432 -> Primeiro digito
    6543298765432 -> Segunro digito


    -----------------------------//// _______ no jeito que eu fiz
    # validação de CNPj

    analise = '04.252.011/0001-10'

    lista_multiplicar = []
    lista_multiplicar2 = []

    lista_nova = []
    lista_nova2 = []

    resultado_da_multiplicao = []


    def parte1():
    global lista_multiplicar
    global lista_nova

    # Aqui to fazendo aprimeira lista
    nova1 = analise.replace('.', '').replace('/', '').replace('-', '')
    nova_lista = list(nova1)

    for i in nova_lista:
        lista_nova.append(int(i))

    # Aqui faz a segunda lista para  ser fator de multiplicação
    for k in range(5, 1, -1):
        lista_multiplicar.append(int(k))
    for i in range(9, 1, -1):
        if i >= 2:
            lista_multiplicar.append(int(i))
        if i == 2:
            break

    print(type(lista_multiplicar), type(lista_nova))

    # fazer  a multiplicação das duas listas e gerando uma terceira lista com so somatorio de toddas duas lista
    #for l in lista_multiplicar:
     #   lala = lista_multiplicar.index(l)
      #  kk = l * lista_nova[lala]

        # print(f'{l} e {lista_nova[lala]}')

       # resultado_da_multiplicao.append(kk)

    # print(f'{lista_multiplicar} {len(lista_multiplicar)}')
    # print(f'{lista_nova} {len(lista_nova)}')
    # print(f'{resultado_da_multiplicao} {len(resultado_da_multiplicao)}')


    def parte2():
    nova2 = analise.replace('.', '').replace('/', '').replace('-', '')
    nova_lista2 = list(nova2)

    for i in nova_lista2:
        lista_nova2.append(int(i))

    for k in range(6, 1, -1):
        lista_multiplicar2.append(k)
    for i in range(9, 1, -1):
        if i >= 2:
            lista_multiplicar2.append(i)
        if i == 2:
            break

    print(lista_nova2, lista_multiplicar2)
    return nova2, lista_multiplicar2


    def parte3():
    global lista_multiplicar
    print(lista_multiplicar)


    parte1()
"""

################ Resolução Da Udemy #######################
