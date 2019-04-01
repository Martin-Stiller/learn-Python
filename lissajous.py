#!/usr/bin/python3.7

import pygame as pg

auflösung = 1000
spalten = 5
abstand = auflösung // spalten
radius = (abstand -20) // 2

pg.init()
screen = pg.display.set_mode([auflösung, auflösung])

weitermachen = True
while weitermachen:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            weitermachen = False
    screen.fill((0,0,0))
    for n in range(spalten):
        pg.draw.circle(screen,(255,255,255),(abstand*n+abstand//2,abstand//2),radius,3)
        pg.draw.circle(screen,(255,255,255),(abstand//2,abstand*n+abstand//2),radius,3)
    pg.display.flip()
pg.quit()
