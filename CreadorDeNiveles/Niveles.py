from CreadorDeNiveles.lectorArchivos import *
class Nivel():
    def __init__(self):
        self.lector = LectorArchivo()

    def crear(self): pass

class NivelFacil(Nivel):
    def crear(self):
        return self.lector.leerNivel("C:/Users/Julian/Documents/UD/4"+ 
        " Semestre/Modelos de Programación/ZombScapeS/CreadorDeNiveles/game.txt")


class NivelMedio(Nivel):
    def crear(self): pass

class NivelDificil(Nivel):
    def crear(self): pass
        