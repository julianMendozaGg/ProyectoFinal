import pygame as p
from pygame import *
from PintarNiveles.Abstraction import *
import random
from CreadorDePersonajes import Poses



class Heroe():
    def __init__(self, ventana):
        self.vida= 100
        self.puntos = 0
        self.velocidad = 9
        self.sentido = 0
        self.obj = ConcreteImplementation1(ventana)
        #copy from set_srpite
        self.obj.pintarNivel()
        self.pos = self.obj.positions[0]
        self.posX = self.pos [0] 
        self.posY = self.pos [1]
        self.rect= p.Rect(self.posX, self.posY , 35, 35)
        self.sprite=Poses

        #copied 
        
        

    def caminoMalo (self):
        self.obj.rectangles #Rectangulos donde no es posible pasar

    
    def moveDer(self,screen):
        pressed = p.key.get_pressed()
        if self.rect.collidelist(self.obj.rectangles) < 0 :
            if pressed[p.K_RIGHT]:
                self.posX = self.posX + self.velocidad
                screen.blit(self.sprite.Der.getSprites(), (self.posX, self.posY))
        else:
            if self.rect.collidelist(self.obj.rectangles) >= 0 and self.posX>700 or pressed[p.K_RIGHT] :
                self.posX= self.posX - 15
                screen.blit(self.sprite.Der.getSprites(), (self.posX, self.posY))
    
    def moverIzq(self,screen):
        pressed =p.key.get_pressed()
        if self.rect.collidelist(self.obj.rectangles) < 0 :
            if pressed[p.K_LEFT]:
                self.posX = self.posX - self.velocidad
                screen.blit(self.sprite.Izq.getSprites(), (self.posX, self.posY))
        else:
            if self.rect.collidelist(self.obj.rectangles) >= 0 and self.posX<140 or pressed[p.K_LEFT]:
                self.posX=self.posX+15
                screen.blit(self.sprite.Izq.getSprites(), (self.posX, self.posY))



    def moveUp(self,screen):
        pressed = p.key.get_pressed()
        if self.rect.collidelist(self.obj.rectangles) < 0:
            if pressed [p.K_UP]:
                self.posY = self.posY - self.velocidad
                screen.blit(self.sprite.Arriba.getSprites(), (self.posX, self.posY))
        else:
            if self.rect.collidelist(self.obj.rectangles) >= 0 and self.posY<140 or pressed[p.K_UP]:
                self.posY=self.posY+15
                screen.blit(self.sprite.Arriba.getSprites(), (self.posX, self.posY))

    def moveDown(self,screen):
        pressed = p.key.get_pressed()

        if self.rect.collidelist(self.obj.rectangles) < 0:
            if pressed[p.K_DOWN]:
                self.posY = self.posY + self.velocidad
                screen.blit(self.sprite.Abajo.getSprites(), (self.posX, self.posY))

        else:
            if self.rect.collidelist(self.obj.rectangles) >= 0 and self.posY > 700 or pressed[p.K_DOWN]:
                self.posY = self.posY - 15
                screen.blit(self.sprite.Abajo.getSprites(), (self.posX, self.posY))

    def update(self,screen):

        self.moveDer(screen)
        self.moverIzq(screen)
        self.moveUp(screen)
        self.moveDown(screen)
        self.rect = p.Rect(self.posX,self.posY,35,35)
        return self.rect
    def drawHero(self,screen):
        screen.blit(self.sprite.Arriba.getSprites(), (self.posX, self.posY))




    

    

        