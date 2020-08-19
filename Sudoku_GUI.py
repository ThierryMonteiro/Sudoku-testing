# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 14:25:57 2020

pyggame GUI for Sudoku

@author: Jun
"""
import pygame, sys
from pygame.locals import *
#from Sudoku_Generator import maker, solution
#from Sudoku_Solver import solve, check, solver

# Window Size - Width has to be a multiple of 9
width = 540
height = 540

# Colors
color = {'black':[0,0,0], 'white':[255,255,255], 'gray': [200,200,200]}

# Draws the grid
def drawGrid():
    square = width // 3
    cell = square // 3
    
    # Square lines
    for i in range(0, width, square): # vertical
        pygame.draw.line(display, color['black'], (i,0),(i,height), 4)
    for j in range(0, height, square): # horizontal
        pygame.draw.line(display, color['black'], (0,j), (width, j), 4)
    
    # Cell Lines
    for i in range(0, width, cell): # vertical
        if i % square != 0:
            pygame.draw.line(display, color['black'], (i,0),(i,height), 1)
    for j in range(0, height, cell): # horizontal
        if j % square != 0:
            pygame.draw.line(display, color['black'], (0,j),(width, j), 1)
    
    return None

# Window + Title + Main Loop
def main():
    global display
    
    pygame.init()
    display = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sudoku")
    display.fill(color['white'])
    
    drawGrid()
    
    # Main Loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == '__main__':
    main()
