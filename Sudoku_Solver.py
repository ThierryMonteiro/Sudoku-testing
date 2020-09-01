# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 20:27:16 2020

Sudoku Solver using Backtracking
Used by generator to create a puzzle
"Solves" an empty board to create a puzzle

@author: Jun
"""
import random

# Uses backtracking to place numbers inside an empty grid
def solve(grid):
    find = is_empty(grid)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1,10):
        i = random.sample(range(1,10),1)[0]
        if check(grid, i, (row, col)):
            grid[row][col] = i
            
            if solve(grid):
                return True
            
            grid[row][col] = ' '
        
    return False

# Solves the puzzle. Used to check if solution and solved puzzle matched
#def solver(grid):
#    find = is_empty(grid)
#    if not find:
#        return True
#    else:
#        row, col = find
#
#    for i in range(1,10):
#        if check(grid, i, (row, col)):
#            grid[row][col] = i
#
#            if solve(grid):
#                return True
#
#            grid[row][col] = 0
#
#    return False

# Checks to see if number placement is valid
def check(grid, num, pos):
   # check row
   if num in row(grid, pos[0]) or num in column(grid, pos[1]) or num in block(grid, pos):
       return False
   return True

# Checks to see if cell is empty
def is_empty(grid): # pos is (i, j) -> (row, column)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == ' ':
                return (i, j)
    return None

# Code below used to access row, column, and block relative to position
def row(grid, row):
    return grid[row]

def column(grid, col):
    return [grid[i][col] for i in range(len(grid))]

def block(grid, pos): # pos is what is_empty returns
# tells you which box it is e.g. the top-left is (0,0)
    box = (pos[0] // 3, pos[1] // 3)                           
    box_num = [
                grid[i][j] 
                for i in range(box[0]*3, box[0]*3 + 3) 
                for j in range(box[1]*3, box[1]*3 + 3)
                ] 
    
    return box_num
    
