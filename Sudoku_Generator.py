# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 21:12:53 2020

Generates a 9x9 Sudoku Puzzle

@author: Jun
"""
from Sudoku_Solver import solve
from random import sample
from copy import deepcopy

def solution():
    grid = [[' ' for n in range(9)] for m in range(9)]
    solve(grid)
    return grid

# Start with an empty grid then "solve" it
def maker():
    sol = solution()
    puzzle = deepcopy(sol)
    # Then take out numbers in the grid. That becomes the puzzle while grid remains
    # as the solution
    
    
    # Randomly replaces cells with 0. You need at least 17 hints or filled in ce;;s
    # to solve a sudoku puzzle so the for loop below randomly erases 17 to 30 cells
    # the 30 limit is arbitrary
    for i in sample(range(81), sample(range(17,31),1)[0]):
        puzzle[i//9][i%9] = ' '
    return puzzle, sol

# formats the puzzle into a more user-friendly format
def format(puzzle):
    print("╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗")
    
    for b in range(len(puzzle)):
        if b % 3 == 0 and b != 0:
            print("╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣")
        if b in [1, 2, 4, 5, 7, 8]:
            print('╟───┼───┼───╫───┼───┼───╫───┼───┼───╢')
        for c in range(len(puzzle[0])):
            if c % 3 == 0:
                print("║ ", end = "")
            if c in [1, 2, 4, 5, 7, 8] and c != 0:
                print('│ ', end = '')
            if c == 8:
                print(str(puzzle[b][c]) + " ║")
            else:
                print(str(puzzle[b][c]) + " ", end = '')
                
    
    print("╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝")
            
if __name__ == '__main__':
    format(maker())

