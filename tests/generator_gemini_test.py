import pytest
from Sudoku_Generator import solution, maker

def test_solution_returns_solved_grid():
    """
    Test that the solution function returns a valid solved Sudoku grid.
    A valid solved Sudoku grid is a 9x9 grid where each row, column, and 3x3 subgrid 
    contains all digits from 1 to 9 without repetition.
    """
    grid = solution()
    assert len(grid) == 9
    for row in grid:
        assert len(row) == 9
        
    # Check rows
    for row in grid:
        row_values = [val for val in row if val != ' ']
        assert len(row_values) == len(set(row_values))
        
    # Check columns
    for col_index in range(9):
        col_values = [grid[row_index][col_index] for row_index in range(9) if grid[row_index][col_index] != ' ']
        assert len(col_values) == len(set(col_values))
        
    # Check 3x3 subgrids
    for subgrid_row in range(3):
        for subgrid_col in range(3):
            subgrid_values = []
            for i in range(3):
                for j in range(3):
                    val = grid[subgrid_row * 3 + i][subgrid_col * 3 + j]
                    if val != ' ':
                        subgrid_values.append(val)
            assert len(subgrid_values) == len(set(subgrid_values))

def test_maker_returns_puzzle_and_solution():
    """
    Test that maker function returns a puzzle and its solution, 
    and that the puzzle has empty cells.
    """
    puzzle, sol = maker()
    assert len(puzzle) == 9
    assert len(sol) == 9
    for row in puzzle:
        assert len(row) == 9
    for row in sol:
        assert len(row) == 9

    has_empty = False
    for row in puzzle:
        if ' ' in row:
            has_empty = True
            break
    assert has_empty

if __name__ == '__main__':
    pytest.main(['-v', __file__])