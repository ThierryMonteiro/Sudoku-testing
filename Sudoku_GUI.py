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
color = {'bl':[0,0,0], 'wh':[255,255,255], 'gr': [200,200,200], 're':[255,0,0],
         'input':[0,128,255]}

# Grid and numbers
square = width // 3
cell = square // 3

# Draws puzzle numbers 
def drawNum(display):  
    x = cell // 2
    y = cell // 2
    for i in puzzle:
        for j in i:
            # inputs are unique in that they're strings which can be used to separate
            # them from the original numbers
            if type(j) == str and j != ' ':
                text = font.render(str(j), True, color['input'])
                display.blit(text, (x-12,y-15))
            elif type(j) == int and j != ' ':      
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
# Returns mouse position
def click(pos):
    if pos[0] < width and pos[1] < height:
        col = pos[0] // cell
        row = pos[1] // cell
        return (int(row),int(col))
    else:
        return None
    
def highlight(pos, display, color, size):
    # Cells get highlighted red once selected
    x, y = pos
    pygame.draw.rect(display, color, (y*cell,x*cell, cell ,cell), size)
    
# Fills in number inputs
def fill_val(display, val, pos):
    x, y = click(pos)
    text = font.render(str(val), 1, color['bl'])
    display.blit(text, (x,y))

# Redraws the board whenever a cell is highlighted to get rid of old highlights
def redrawer():
    display.fill(color['wh'])
    drawGrid()
    drawNum(display)
    
# Window + Title + Main Loop
def main():
    global display
    
    display = pygame.display.set_mode((width, height))
    
    pygame.display.set_caption("Sudoku")
    display.fill(color['wh'])
    key = None
    run = True
    select = False
    
    drawGrid()
    drawNum(display)
    
    # Main Loop
    while run:
        for event in pygame.event.get():         
            if event.type == QUIT:
                pygame.quit()
                run = False
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
                select = True
                pos = pygame.mouse.get_pos()
                if pos:
                    redrawer()
                    highlight(click(pos), display, color['re'], 2)
                    key = None  
                    
        # Takes input and updates puzzle with it so it won't get erased
        # Input numbers are unique in that they're strings. This is so drawNum
        # colors them blue instead of black
        if select == True and key != None:
            row, col = click(pos)
            # Only draws numbers if you click on an empty cell
            if puzzle[row][col] == ' ' or type(puzzle[row][col]) == str:
                puzzle[row][col] = str(key)
                # If you're correct, the solution cell also changes to an str
                # This for an easier comparison later when I add a check solution button
                if solu[row][col] == key:
                    solu[row][col] = str(key)
                redrawer()
                text = font.render(str(key), True, color['input'])
                display.blit(text, (col*cell+18, row*cell+15))
            
            

        pygame.display.update()


if __name__ == '__main__':
    main()
    
