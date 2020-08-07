import pygame as p
class ChainMusic():
    def __init__(self):
        self.__sucesor__ = None
        p.mixer.init()

    def handlerRequest(self,key): pass

    def setSucesor(self):
        self.__sucesor__ = sucesor

class HandlerKey0(ChainMusic):
    def handlerRequest(self, key):
        p.mixer.music.load("C:/Users/Julian/Documents/UD/4 Semestre/Modelos de Programación/ZombScapeS/music/0.mp3")
        if key == p.K_0:
            p.mixer.music.play()
        else:
            self.__sucesor__.handlerRequest(key)
    
class HandlerKey1(ChainMusic):
    def handlerRequest(self, key):
        p.mixer.music.load("")
        



            
        