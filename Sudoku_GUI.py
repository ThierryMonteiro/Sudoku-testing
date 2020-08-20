# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 14:25:57 2020

pyggame GUI for Sudoku

@author: Jun
"""
import pygame, sys
from pygame.locals import *
from Sudoku_Generator import maker
from Sudoku_Solver import solve, check, solver
pygame.font.init()

puzzle, solu = maker()

# Window Size - Width has to be a multiple of 9
width = 540
height = 540

# Colors
color = {'bl':[0,0,0], 'wh':[255,255,255], 'gr': [200,200,200]}

# Grid and numbers
square = width // 3
cell = square // 3

# Draws puzzle numbers 
def drawNum(display):
    font = pygame.font.SysFont('comicsans', 60)
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
    

# Window + Title + Main Loop
def main():
    global display
    

    display = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sudoku")
    display.fill(color['wh'])
    
    drawGrid()
    drawNum(display)
    
    # Main Loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == '__main__':
    main()
