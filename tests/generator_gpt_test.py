import pytest
from unittest.mock import patch
from copy import deepcopy


import sys
import os

# Add project root to Python path to import Sudoku_solver
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa o arquivo a ser testado
import Sudoku_Generator as sg

# Teste para solution(), usando mock para a função solve
@patch("Sudoku_Generator.solve")
def test_solution(mock_solve):
    def mock_solve_impl(grid):
        for i in range(9):
            for j in range(9):
                grid[i][j] = i * 9 + j + 1  # Valor único só para testar

    mock_solve.side_effect = mock_solve_impl

    result = sg.solution()
    assert len(result) == 9
    assert all(len(row) == 9 for row in result)
    assert all(cell != ' ' for row in result for cell in row)

# Teste para maker()
@patch("Sudoku_Generator.solve")
def test_maker(mock_solve):
    def mock_solve_impl(grid):
        for i in range(9):
            for j in range(9):
                grid[i][j] = 1  # valor qualquer

    mock_solve.side_effect = mock_solve_impl

    puzzle, solution = sg.maker()
    assert len(puzzle) == 9
    assert all(len(row) == 9 for row in puzzle)
    # A solução deve ter só 1s
    assert all(cell == 1 for row in solution for cell in row)
    # O puzzle deve ter ao menos 17 células preenchidas
    filled = sum(cell != ' ' for row in puzzle for cell in row)
    assert filled >= 17

# Teste básico para format: só valida que não quebra
@patch("Sudoku_Generator.solve")
def test_format(mock_solve, capsys):
    def mock_solve_impl(grid):
        for i in range(9):
            for j in range(9):
                grid[i][j] = 1

    mock_solve.side_effect = mock_solve_impl
    puzzle, _ = sg.maker()
    sg.format(puzzle)
    captured = capsys.readouterr()
    assert "╔═══╤═══╤═══╦" in captured.out
