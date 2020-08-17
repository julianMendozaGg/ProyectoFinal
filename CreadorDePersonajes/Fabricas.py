from CreadorDePersonajes.Poses import *
class AbstractFactory():
    def moverArriba(self): pass
    def moverDer(self): pass
    def moverAbajo(self): pass
    def moverIzq(self): pass
    def power(self): pass

class WarriorFactory(AbstractFactory):

    def moverAbajo():
        abajo = AbajoWarrior()
        return abajo.getSprites()

    def moverArriba():
        arriba = ArribaWarrior()
        return arriba.getSprites()

    def moverDer():
        der = DerWarrior()
        return der.getSprites()

    def moverIzq():
        izq = IzqWarrior()
        return izq.getSprites()

class QueenFactory(AbstractFactory):

    def moverAbajo():
        abajo = AbajoQueen()
        return abajo.getSprites()

    def moverArriba():
        arriba = ArribaQueen()
        return arriba.getSprites()

    def moverDer():
        der = DerQueen()
        return der.getSprites()

    def moverIzq():
        izq = IzqQueen()
        return izq.getSprites()