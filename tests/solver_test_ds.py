import pytest
from Sudoku_Solver import solve, check, is_empty, row, column, block

def test_is_empty():
    """
    Testa se a função is_empty() identifica corretamente células vazias e retorna None quando a grade está completa.
    """
    # Grade com célula vazia
    grid_with_empty = [
        ['1', ' ', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]
    assert is_empty(grid_with_empty) == (0, 1), "Deveria retornar a posição (0, 1)."

    # Grade sem células vazias
    grid_full = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]
    assert is_empty(grid_full) is None, "Deveria retornar None para grade completa."

def test_row():
    """
    Testa se a função row() retorna a linha correta da grade.
    """
    grid = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]
    assert row(grid, 1) == ['4', '5', '6'], "Deveria retornar a segunda linha."

def test_column():
    """
    Testa se a função column() retorna a coluna correta da grade.
    """
    grid = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]
    assert column(grid, 0) == ['1', '4', '7'], "Deveria retornar a primeira coluna."

def test_block():
    """
    Testa se a função block() retorna o bloco 3x3 correto da grade.
    """
    grid = [
        ['1', '2', '3', ' ', ' ', ' ', ' ', ' ', ' '],
        ['4', '5', '6', ' ', ' ', ' ', ' ', ' ', ' '],
        ['7', '8', '9', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    assert block(grid, (0, 0)) == ['1', '2', '3', '4', '5', '6', '7', '8', '9'], "Deveria retornar o bloco superior esquerdo."

def test_check():
    """
    Testa se a função check() valida corretamente a inserção de números.
    """
    grid = [
        ['1', '2', '3', ' ', ' ', ' ', ' ', ' ', ' '],
        ['4', '5', '6', ' ', ' ', ' ', ' ', ' ', ' '],
        ['7', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    # Testa inserção válida
    assert check(grid, 9, (2, 2)) is True, "Deveria permitir inserir 9 na posição (2, 2)."
    # Testa inserção inválida (número já na linha)
    assert check(grid, 1, (0, 3)) is False, "Deveria bloquear inserção de 1 na linha 0."
    # Testa inserção inválida (número já no bloco)
    assert check(grid, 5, (2, 2)) is False, "Deveria bloquear inserção de 5 no bloco."

def test_solve():
    """
    Testa se a função solve() resolve corretamente uma grade vazia.
    """
    grid = [[' ' for _ in range(9)] for _ in range(9)]
    assert solve(grid) is True, "Deveria resolver a grade vazia."
    for row in grid:
        assert ' ' not in row, "Todas as células deveriam estar preenchidas após solve()."