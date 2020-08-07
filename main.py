import pygame as p
import sys
from Board import *
from music.chainMusic import *

ventana = p.display.set_mode ((650,600))
board = Board(ventana)
p.display.set_caption("zombIES")
state = True
z=30
NEGRO = (0,0,0)
p.mixer.init()
p.mixer.music.load("C:/Users/Julian/Documents/UD/4 Semestre/Modelos de Programación/ZombScapeS/music/sound.mp3")
soundFx= HandlerKey0()
p.mixer.music.play()

while state:
    for event in p.event.get():
        if event.type == p.QUIT:
            sys.exit()
        if event.type == p.KEYDOWN:
            soundFx.handlerRequest(event.key)

    ventana.fill(NEGRO)
    board.pintar()
    
    p.display.update()
    