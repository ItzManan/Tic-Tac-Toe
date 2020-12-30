import pygame as pg
import sys

from pygame import mouse

pg.init()

screen = pg.display.set_mode((500, 500))

pg.display.set_caption("Tic-Tac-Toe")

grid = pg.image.load("Grid.png")

icon = pg.image.load("Window_icon.png")

x = pg.image.load("X.png")

o = pg.image.load("O.png")

pg.display.set_icon(icon)

moves = 0


def bg():
    screen.blit(grid, (0, 0))


running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            moves +=1
            mouse_pos = pg.mouse.get_pos()

    bg()

    pg.display.update()

pg.quit()
sys.exit()
