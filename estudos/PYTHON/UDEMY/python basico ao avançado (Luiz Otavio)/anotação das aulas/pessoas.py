# Metodos = são função que pertecente a uma classe

class Pessoas:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self):
        if self.comendo:
            print(f'{self.nome} já estar comendo ')
            return
        if self.falando:
            print(f'{self.nome} ele ja estar falando ')
            return
        print(f'{self.nome} ja estar falando')
        self.falando = True

    def comer(self, alimento):

        if self.comendo:
            print(f'{self.nome} já estar comendo.')
            return

        print(f'{self.nome} estar comendo {alimento}')
        self.comendo = True

    def para_de_comer(self):
        if not self.comendo:
            print(f'{self.nome} não estar comendo ')
            return
        print(f'{self.nome} parou de comer ')
        self.comendo = False
