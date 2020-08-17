from CreadorDePersonajes import LoadImages
loadImages=LoadImages
class Izq():
    def getSprites():
        return loadImages.load("Imagenes/capezaper2.png")


class Der():
    def getSprites():
        return loadImages.load("Imagenes/cabezaper.png")


class Arriba():
    def getSprites():
        return loadImages.load("Imagenes/capezaperd.png")


class Abajo ():
    def getSprites():
        return loadImages.load("Imagenes/capezapera.png")


class IzqWarrior(Izq):
    def getSprites():
        return super().getSprites()


class DerWarrior(Der):
    def getSprites():
        return super().getSprites()


class ArribaWarrior(Arriba):
    def getSprites():
        return super().getSprites()


class AbajoWarrior(Abajo):
    def getSprites():
        return super().getSprites()


class IzqQueen(Izq):
    def getSprites():
        return super().getSprites()


class DerQueen(Der):
    def getSprites():
        return super().getSprites()


class ArribaQueen(Arriba):
    def getSprites():
        return super().getSprites()


class AbajoQueen(Abajo):
    def getSprites():
        return super().getSprites()
