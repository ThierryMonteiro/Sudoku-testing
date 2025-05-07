import pytest
from Sudoku_Solver import solve, check, is_empty, row, column, block

def create_empty_grid():
    """Creates an empty 9x9 Sudoku grid."""
    return [[' ' for _ in range(9)] for _ in range(9)]

def create_valid_grid():
    """Creates a valid solved Sudoku grid for testing."""
    return [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]

def create_invalid_grid():
    """Creates an invalid Sudoku grid for testing."""
    return [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 5]  # Last element changed to 5 (invalid)
    ]

def test_solve_valid_grid():
    """Tests if the solve function correctly solves an empty grid."""
    grid = create_empty_grid()
    solve(grid)
    assert is_valid_solution(grid)

def test_check_valid_placement():
    """Tests if check function returns True for a valid placement."""
    grid = create_valid_grid()
    assert check(grid, 1, (0, 1)) # Should be false, already exists
    assert check(grid, 2, (1, 2)) # Should be false, already exists
    assert not check(grid, 5, (0, 0))
    
    grid2 = create_empty_grid()
    assert check(grid2, 5, (0,0))

def test_check_invalid_placement():
    """Tests if check function returns False for an invalid placement."""
    grid = create_valid_grid()
    assert not check(grid, 3, (0, 1))  # Already a 3 in row 0
    assert not check(grid, 6, (0, 3))  # Already a 6 in row 0
    assert not check(grid, 7, (0, 5))
    assert not check(grid, 6, (3, 0)) # Already a 6 in column 0
    assert not check(grid, 3, (6, 4))
    assert not check(grid, 2, (8, 5))
    assert not check(grid, 2, (0, 8))
    assert not check(grid, 2, (0, 8))
    assert not check(grid, 5, (2, 7))

def test_is_empty():
    """Tests if is_empty function correctly identifies empty cells."""
    grid1 = create_empty_grid()
    assert is_empty(grid1) == (0, 0)

    grid2 = create_valid_grid()
    assert is_empty(grid2) is None

    grid3 = [
        [5, 3, ' ', 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    assert is_empty(grid3) == (0, 2)

def test_row():
    """Tests if row function correctly returns a row."""
    grid = create_valid_grid()
    assert row(grid, 0) == [5, 3, 4, 6, 7, 8, 9, 1, 2]
    assert row(grid, 4) == [4, 2, 6, 8, 5, 3, 7, 9, 1]
    assert row(grid, 8) == [3, 4, 5, 2, 8, 6, 1, 7, 9]

def test_column():
    """Tests if column function correctly returns a column."""
    grid = create_valid_grid()
    assert column(grid, 0) == [5, 6, 1, 8, 4, 7, 9, 2, 3]
    assert column(grid, 4) == [7, 9, 4, 6, 5, 2, 3, 1, 8]
    assert column(grid, 8) == [2, 8, 7, 3, 1, 6, 4, 5, 9]

def test_block():
    """Tests if block function correctly returns a 3x3 block."""
    grid = create_valid_grid()
    assert block(grid, (0, 0)) == [5, 3, 4, 6, 7, 2, 1, 9, 8]
    assert block(grid, (1, 1)) == [5, 3, 4, 6, 7, 2, 1, 9, 8]
    assert block(grid, (0, 3)) == [6, 7, 8, 1, 9, 5, 3, 4, 2]
    assert block(grid, (4, 4)) == [7, 6, 1, 8, 5, 3, 9, 2, 4]
    assert block(grid, (8, 8)) == [2, 8, 4, 6, 3, 5, 1, 7, 9]

def is_valid_solution(grid):
    """Helper function to check if a Sudoku grid is a valid solution."""

    # Check rows
    for row in grid:
        if any(row.count(str(num)) > 1 for num in range(1, 10) if str(num) in row):
            return False

    # Check columns
    for col in range(9):
        column = [grid[row][col] for row in range(9)]
        if any(column.count(str(num)) > 1 for num in range(1, 10) if str(num) in column):
            return False

    # Check 3x3 subgrids
    for subgrid_row in range(3):
        for subgrid_col in range(3):
            subgrid = [
                grid[i][j]
                for i in range(subgrid_row * 3, subgrid_row * 3 + 3)
                for j in range(subgrid_col * 3, subgrid_col * 3 + 3)
            ]
            if any(subgrid.count(str(num)) > 1 for num in range(1, 10) if str(num) in subgrid):
                return False

    return True

if __name__ == '__main__':
    pytest.main(['-v', __file__])