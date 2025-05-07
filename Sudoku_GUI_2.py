# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 14:25:57 2020

pyggame GUI for Sudoku (modificado com redimensionamento de janela)

@author: Jun / Modificado por ChatGPT
"""
import pygame, sys
from pygame.locals import *
from Sudoku_Generator import maker, format

pygame.font.init()
font = pygame.font.SysFont('comicsans', 60)

# Tamanho fixo do tabuleiro e extensão da área inferior
width = 639
height = 639
ex = 100

# Cores
color = {'bl':[0,0,0], 'wh':[255,255,255], 'gr': [200,200,200], 're':[255,0,0],
         'input':[0,128,255], 'solu':[0,204,102], 'hover':[204,255,229]}

# Tamanhos dos quadrados
square = width // 3
cell = square // 3

# Desenhar números
def drawNum(puzzle, solu, soluOn, surface):  
    x = cell // 2
    y = cell // 2
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            num = puzzle[i][j]
            if type(num) == str and num != ' ' and soluOn == True:
                text = font.render(str(solu[i][j]), True, color['input'])
                surface.blit(text, (x-12,y-15))
            elif type(num) == str and num != ' ':
                text = font.render(str(num), True, color['input'])
                surface.blit(text, (x-12,y-15))
            elif type(num) == int and num != ' ':      
                text = font.render(str(num), True, color['bl'])
                surface.blit(text, (x-12,y-15))
            elif num == ' ' and soluOn == True:
                text = font.render(str(solu[i][j]), True, color['re'])
                surface.blit(text, (x-12,y-15))
            x += cell
        x = cell // 2
        y += cell 

# Desenhar grade
def drawGrid(surface): 
    for i in range(0, width, square):
        if i != 0:
            pygame.draw.line(surface, color['bl'], (i,0),(i,height), 4)
    for j in range(0, height, square):
        if j != 0:
            pygame.draw.line(surface, color['bl'], (0,j), (width, j), 4)
    for i in range(0, width, cell):
        if i % square != 0:
            pygame.draw.line(surface, color['bl'], (i,0),(i,height), 1)
    for j in range(0, height, cell):
        if j % square != 0:
            pygame.draw.line(surface, color['bl'], (0,j),(width, j), 1)
    pygame.draw.line(surface, color['bl'], (0,height), (width, height), 4)

# Botões
def checkSolu(surface):
    x_solu = width // 2 - cell
    y_solu = (height+ex)-77
    x_new = width // 6 - cell
    y_new = y_solu
    pygame.draw.rect(surface, color['bl'], (x_solu, y_solu, cell*2, cell), 3)
    text = font.render('Solve', True, color['solu'])
    surface.blit(text, (x_solu+5, y_solu+10))
    pygame.draw.rect(surface, color['bl'], (x_new, y_new, cell*2, cell), 3)
    text = font.render('New', True, color['solu'])
    surface.blit(text, (x_new+15, y_new+10))

# Clique
def click(pos):
    if pos[0] < width and pos[1] < height:
        col = pos[0] // cell
        row = pos[1] // cell
        return (int(row),int(col))
    else:
        return None

def highlight(pos, surface):
    try:
        x, y = pos
        pygame.draw.rect(surface, color['re'], (y*cell,x*cell, cell ,cell), 2)
    except TypeError:
        pass

def redrawer(puzzle, solu, soluOn, surface):
    surface.fill(color['wh'])
    drawGrid(surface)
    drawNum(puzzle, solu, soluOn, surface)
    checkSolu(surface)

# Loop principal
def main():
    global display
    puzzle, solu = maker()
    display = pygame.display.set_mode((width, height + ex), pygame.RESIZABLE)
    pygame.display.set_caption("Sudoku")
    key = None
    run = True
    select = False
    soluOn = False
    pos = None

    if (width <= 864):
        surface = pygame.Surface((width, height + ex))
    else:
        surface = pygame.Surface((864, 864 + ex))
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            elif event.type == pygame.KEYDOWN:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    key = event.key - pygame.K_0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                win_w, win_h = display.get_size()
                offset_x = (win_w - width) // 2
                offset_y = (win_h - (height + ex)) // 2
                mouse_x, mouse_y = event.pos
                adj_x = mouse_x - offset_x
                adj_y = mouse_y - offset_y
                pos = (adj_x, adj_y)
                select = True
                if 0 <= adj_x < width and 0 <= adj_y < height:
                    redrawer(puzzle, solu, soluOn, surface)
                    highlight(click(pos), surface)
                    key = None 
                if width // 2 - cell + cell*2 > adj_x > width // 2 - cell and (height+ex)-77 + cell > adj_y > (height+ex)-77:
                    soluOn = True
                    redrawer(puzzle, solu, soluOn, surface)
                if width // 6 - cell + cell*2 > adj_x > width // 6 - cell and (height+ex)-77 + cell > adj_y > (height+ex)-77:
                    puzzle, solu = maker()
                    soluOn = False
                    redrawer(puzzle, solu, soluOn, surface)

        if select and key is not None and pos:
            adj_x, adj_y = pos
            if 0 <= adj_x < width and 0 <= adj_y < height:
                row, col = click((adj_x, adj_y))
                if puzzle[row][col] == ' ' or type(puzzle[row][col]) == str:
                    puzzle[row][col] = str(key)
                    if solu[row][col] == key:
                        solu[row][col] = str(key)
                    redrawer(puzzle, solu, soluOn, surface)

        redrawer(puzzle, solu, soluOn, surface)
        win_w, win_h = display.get_size()
        offset_x = (win_w - width) // 2
        offset_y = (win_h - (height + ex)) // 2
        display.fill(color['wh'])
        display.blit(surface, (offset_x, offset_y))
        pygame.display.update()

if __name__ == '__main__':
    main()