# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 14:25:57 2020

pyggame GUI for Sudoku

@author: Jun
"""
import pygame, sys
from pygame.locals import *
from Sudoku_Generator import maker
pygame.font.init()

puzzle, solu = maker()

font = pygame.font.SysFont('comicsans', 60)
# Window Size - Width has to be a multiple of 9
width = 540
height = 540

# Colors
color = {'bl':[0,0,0], 'wh':[255,255,255], 'gr': [200,200,200], 're':[255,0,0]}

# Grid and numbers
square = width // 3
cell = square // 3

# Draws puzzle numbers 
def drawNum(display):  
    x = cell // 2
    y = cell // 2
    for i in puzzle:
        for j in i:
            if j != ' ':      
                text = font.render(str(j), True, color['bl'])
                display.blit(text, (x-12,y-15))
            x += cell
        x = cell // 2
        y += cell 
              
# Draws the grid
def drawGrid(): 
    # Square lines
    for i in range(0, width, square): # vertical
        if i != 0:
            pygame.draw.line(display, color['bl'], (i,0),(i,height), 4)
    for j in range(0, height, square): # horizontal
        if j != 0:
            pygame.draw.line(display, color['bl'], (0,j), (width, j), 4)
    
    # Cell Lines
    for i in range(0, width, cell): # vertical
        if i % square != 0:
            pygame.draw.line(display, color['bl'], (i,0),(i,height), 1)
    for j in range(0, height, cell): # horizontal
        if j % square != 0:
            pygame.draw.line(display, color['bl'], (0,j),(width, j), 1)

#### Not finished    
#def highlight(display):
#    # Cells get highlighted red once selected
#    pygame.draw.rect(display, color['re'], (x,y, gap ,gap), 3)
def click(pos):
    if pos[0] < width and pos[1] < height:
        x = pos[0] // cell
        y = pos[1] // cell
        return (int(x),int(y))
    else:
        return None
# Fills in number inputs
def fill_val(display, val, pos):
    x, y = click(pos)
    text = font.render(str(val), 1, color['bl'])
    display.blit(text, (x,y))
    
# Window + Title + Main Loop
def main():
    global display
    

    display = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sudoku")
    display.fill(color['wh'])
    key = None
    
    drawGrid()
    drawNum(display)
    
    # Main Loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                key = None
                
        pygame.display.update()


if __name__ == '__main__':
    main()
