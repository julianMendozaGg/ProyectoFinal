import pygame as p
import sys
from Board import *
from Musica.chainMusic import *
from Musica.AsignarSucesor import *
from Heroe import *
from CreadorDePersonajes import Poses

ventana = p.display.set_mode ((900,800),p.RESIZABLE)

board = Board(ventana)
p.display.set_caption("zombIES")
state = True
z=30
NEGRO = (0,0,0)
soundFx = Asigandora()
perso = Heroe(ventana)
timer = p.time.Clock()
sprite=Poses


while state:
    for event in p.event.get():

        if event.type == p.QUIT:
            sys.exit()
        if event.type == p.KEYDOWN:
            soundFx.listaSucesores[0].handlerRequest(event.key)



    ventana.fill(NEGRO)
    board.pintar()

    perso.update(ventana)
    if event.type == p.KEYUP:
        perso.drawHero(ventana)


    # Falta que la imagens e mantenga

    timer.tick(40)
    p.display.update()

    
    