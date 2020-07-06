import os
import time

secreto = 'lucas'
digitado = []
chance = 3
x = 0
while True:
    if chance <= 0 :
        print("Você PerDeu !!! ")
        break
    letra = input("Digite uma letra : ")

    if len(letra) >1 :
        print("Não vale você so pode tentar uma letra por vez !!!!!!!!! ")
        continue

    digitado.append(letra)

    if letra in secreto :
        print(f' Massa, essa letra "{letra}"  existe na palavra magica.')
    else:
        print(f'Essa letra "{letra}" NÃO EXISTE NA PALAVRA !!!! ')
        digitado.pop()

    secreto_temporario = ''

    for letra in secreto :
        if letra in digitado:
            secreto_temporario += letra
        else :
            secreto_temporario += '*'
    print(secreto_temporario)

    if letra not in secreto:
        chance -= 1
    print(f"Você tem {chance} chances de erra !! ")

    if secreto_temporario == secreto:
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')
        time.sleep(0.9)





'''
    if secreto_temporario == secreto :
        print(f'Você  GANHOU O JOGO  a palavra magica foi {secreto}')
        break
    else:
        print(f'A palavra era {secreto},  você Perdeu :( ')
'''

