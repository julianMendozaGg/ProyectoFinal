from CreadorDeNiveles.lectorArchivos import *
class Nivel():
    def __init__(self):
        self.lector = LectorArchivo()

    def crear(self): pass

class NivelFacil(Nivel):
    def crear(self):
        return self.lector.devolverMatriz("C:/Users/Julian/Documents/UD/4"+ 
        " Semestre/Modelos de Programación/pruebaMatrices/CreadorDeNiveles/game.txt")


class NivelMedio(Nivel):
    def crear(self): pass

class NivelDificil(Nivel):
    def crear(self): pass
        