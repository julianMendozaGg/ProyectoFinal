import pygame as p
import sys

ventana = p.display.set_mode ((500,500))
p.display.set_caption("zombIES")
state = True


while state:
    for event in p.event.get():
        
        if event.type == p.QUIT:
            sys.exit()