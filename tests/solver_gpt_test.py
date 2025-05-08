import pytest

import sys
import os

# Add project root to Python path to import Sudoku_solver
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from Sudoku_Solver import solve, check, is_empty, row, column, block

@pytest.fixture
def empty_grid():
    return [[' ' for _ in range(9)] for _ in range(9)]

@pytest.fixture
def partial_grid():
    grid = [[' ' for _ in range(9)] for _ in range(9)]
    grid[0][0] = 5
    grid[1][1] = 5
    grid[0][1] = 3
    return grid

def test_is_empty(empty_grid):
    assert is_empty(empty_grid) == (0, 0)
    empty_grid[0][0] = 1
    assert is_empty(empty_grid) == (0, 1)

def test_row():
    grid = [[i for i in range(9)] for _ in range(9)]
    print(grid)
    assert row(grid, 0) == list(range(9))
    assert row(grid, 3) == list(range(9))

def test_column():
    grid = [[j for j in range(9)] for j in range(9)]
    print(grid)
    assert column(grid, 0) == list(range(9))
    assert column(grid, 5) == [5 for _ in range(9)]

def test_block():
    grid = [[0]*9 for _ in range(9)]
    grid[0][0] = 1
    grid[1][1] = 2
    grid[2][2] = 3
    assert set(block(grid, (0, 0))) == {0, 1, 2, 3}

def test_check_valid():
    grid = [[' ' for _ in range(9)] for _ in range(9)]
    grid[0][0] = 5
    assert not check(grid, 5, (0, 1))  # Mesma linha
    assert check(grid, 4, (0, 1))

def test_solve_returns_true_on_empty_grid(empty_grid):
    result = solve(empty_grid)
    assert result is True
    # Confirma que não há espaços vazios
    assert is_empty(empty_grid) is None

def test_solve_valid_solution(empty_grid):
    solve(empty_grid)
    # Cada linha, coluna e bloco deve conter todos os números de 1 a 9
    for i in range(9):
        assert sorted(row(empty_grid, i)) == list(range(1, 10))
        assert sorted(column(empty_grid, i)) == list(range(1, 10))
    for i in range(3):
        for j in range(3):
            pos = (i * 3, j * 3)
            assert sorted(block(empty_grid, pos)) == list(range(1, 10))
