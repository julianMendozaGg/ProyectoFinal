import pygame as p
import sys
from Board import *

ventana = p.display.set_mode ((500,500))
board = Board(ventana)
p.display.set_caption("zombIES")
state = True
z=30
NEGRO = (0,0,0)


while state:
    for event in p.event.get():
        if event.type == p.QUIT:
            sys.exit()
    ventana.fill(NEGRO)
    board.pintar()
    
    p.display.update()
    