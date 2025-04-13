import pytest
from copy import deepcopy
import sys
import os

# Add project root to Python path to import Sudoku_solver
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Sudoku_Solver  # Now we can import it properly

@pytest.fixture
def empty_board():
    return [[' ' for _ in range(9)] for _ in range(9)]

@pytest.fixture
def partially_filled_board():
    board = [[' ' for _ in range(9)] for _ in range(9)]
    board[0][0] = 5
    board[1][1] = 3
    board[2][2] = 7
    return board

def test_is_empty_returns_first_empty_cell(empty_board):
    assert Sudoku_Solver.is_empty(empty_board) == (0, 0)

def test_is_empty_returns_none_when_full():
    full_board = [[i for i in range(1, 10)] for _ in range(9)]
    assert Sudoku_Solver.is_empty(full_board) is None

def test_check_valid_move(partially_filled_board):
    assert Sudoku_Solver.check(partially_filled_board, 1, (0, 1)) is True

def test_check_invalid_due_to_row(partially_filled_board):
    assert Sudoku_Solver.check(partially_filled_board, 5, (0, 1)) is False

def test_check_invalid_due_to_column(partially_filled_board):
    assert Sudoku_Solver.check(partially_filled_board, 3, (0, 1)) is False

def test_check_invalid_due_to_block(partially_filled_board):
    assert Sudoku_Solver.check(partially_filled_board, 3, (1, 2)) is False

def test_solve_empty_board(empty_board):
    board_copy = deepcopy(empty_board)
    solved = Sudoku_Solver.solve(board_copy)
    assert solved is True
    for row in board_copy:
        assert sorted(row) == list(range(1, 10))  # Row must have 1-9 with no duplicates

def test_solve_does_not_change_completed_board():
    board = [
        [5,3,4,6,7,8,9,1,2],
        [6,7,2,1,9,5,3,4,8],
        [1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],
        [4,2,6,8,5,3,7,9,1],
        [7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],
        [2,8,7,4,1,9,6,3,5],
        [3,4,5,2,8,6,1,7,9]
    ]
    assert Sudoku_Solver.solve(board) is True
    # The board should remain the same
    assert board == [
        [5,3,4,6,7,8,9,1,2],
        [6,7,2,1,9,5,3,4,8],
        [1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],
        [4,2,6,8,5,3,7,9,1],
        [7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],
        [2,8,7,4,1,9,6,3,5],
        [3,4,5,2,8,6,1,7,9]
    ]


def test_solve_partially_filled_board():
    board = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [4, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]
    assert Sudoku_Solver.solve(board) is True
    for row in board:
        assert sorted(row) == list(range(1, 10))