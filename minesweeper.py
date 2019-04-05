import pygame as pg 
auflösung = 1000
raster = 9
abstand = auflösung // raster

pg.init()
screen  = pg.display.set_mode([auflösung, auflösung])
cell_normal = pg.image.load('minesweeper_gif/ms_button_normal.gif')
screen.blit(cell_normal,(100,100))
while True :
    pg.display.flip()

anzMinen = 10
matrix =[]

class Cell():
    spalte : int
    zeile : int
    mine : bool = False
    selected : bool = False
    flagged : bool = False
    anzMinenDrumrum : int = 0

def show(self):
    pass
