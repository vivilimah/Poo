import random

class OVNI:
    def __init__(self, label, x, vida):
        if vida <= 0:
            self.vivo = False
        else:
            self.label = label
            self.x = x
            self.vida = vida
            self.vivo = True

    def andar(self):
        if self.vida == "Morreu":
            self.x = 0
        elif(random.randint(0, 1) == 0):
            self.x = self.x - 1
        else:
            self.x = self.x + 1

    def apanhar(self, forca):
        if self.vida <= 0:
            self.vida = "Morreu"
            self.vivo = False
        else:
            self.vida -= forca
    def __str__(self):
        if self.vivo == False:
            return "Nave Atingida"
        else:
            return self.label + " " + str(self.x) \
                    + " (" + str(self.vida) + ")"


class Nave:
    def __init__(self, x, forca):
        self.x = x
        self.forca = forca

    def atirar(self, lista_ovni):
        for ovni in lista_ovni:
            if ovni.x == self.x:
                ovni.apanhar(self.forca)

    def mover(self, desl):
        self.x += desl

    def __str__(self):
        return "Nave:" + str(self.x)

nave = Nave(5, 1)

print "ESCOLHA O NUMERO DE VIDA DE CADA OVNI"
ovni1 = input("OVNI 1: ")
ovni2 = input("OVNI 2: ")

lista = [OVNI("OVNI 1", 2, ovni1), OVNI("OVNI 2", 6, ovni2)]
tiro = 0
jogo = True
while(jogo == True):
    print(nave)
    for x in lista:
        print(x)
            
    print "Total de tiros dados: ", tiro
    escolha = raw_input("deax: ")
    if escolha == "d":
        nave.mover(1)
    elif escolha == "e":
        nave.mover(-1)
    elif escolha == "a":
        tiro += 1
        nave.atirar(lista)
    for x in lista:
        x.andar()