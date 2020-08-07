from CreadorDeNiveles.Creador import *
import pygame as p
class Abstraction():
    def __init__(self, ventana):
        self.ventana = ventana
       
    def entregarlvl1(self):
        lvl1= ConcreteImplementation1(self.ventana)
        return lvl1.pintarNivel()

    def entregarlvl2(self): pass
    def entregarlvl3(self): pass


class Implementation():
    def __init__(self, ventana):
        self.VERDE = (15,255,8)
        self.ROJO =(255,0,0)
        self.ventana = ventana
        self.X=50
        self.Y=50


    def pintarNivel(self): pass

class ConcreteImplementation1(Implementation):
    def pintarNivel(self):
        creat = CreadorNivelFacil()
        prod = creat.diseñarNivel().crear()
        
        for i in range(len(prod)-1):
            for j in range (len(prod)-1):
                if prod[i][j] == "0":
                    p.draw.rect(self.ventana,self.VERDE,(self.X,self.Y,70,70))
                elif prod [i][j] == "1":
                    p.draw.rect(self.ventana,self.ROJO,(self.X,self.Y,70,70))

                self.X = self.X + 50
            
            self.Y= self.Y + 50
            self.X=50
        
                
        