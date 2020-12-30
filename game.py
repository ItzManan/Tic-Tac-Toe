import pygame as pg
import sys

from pygame import mouse

pg.init()

screen = pg.display.set_mode((500, 500))

pg.display.set_caption("Tic-Tac-Toe")

grid = pg.image.load("Grid.png")

icon = pg.image.load("Window_icon.png")

x_img = pg.image.load("X.png")

o_img = pg.image.load("O.png")

pg.display.set_icon(icon)

moves = 0


def bg():
    screen.blit(grid, (0, 0))

def move(x, y):
    global moves
    global screen
    if moves % 2 == 1:
        screen.blit(o_img, (x, y))
    else:
        screen.blit(x_img, (x, y))

running = True

while running:
    screen.fill((255, 255, 255))
    bg()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            moves +=1
            mouse_x, mouse_y = pg.mouse.get_pos()
            move(mouse_x, mouse_y)
            
            
    

    pg.display.update()

pg.quit()
sys.exit()
