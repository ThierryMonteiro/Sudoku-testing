import pytest
from Sudoku_Generator import solution, maker, format
from copy import deepcopy

def test_solution():
    """
    Testa se a função solution() retorna uma grade 9x9 válida preenchida com números.
    """
    grid = solution()
    assert len(grid) == 9, "A grade deve ter 9 linhas."
    for row in grid:
        assert len(row) == 9, "Cada linha deve ter 9 colunas."
        for cell in row:
            assert cell != ' ', "Todas as células devem estar preenchidas com números."

def test_maker():
    """
    Testa se a função maker() retorna uma grade de puzzle e uma solução válidas.
    Verifica também se o puzzle tem pelo menos 17 células preenchidas.
    """
    puzzle, sol = maker()
    assert len(puzzle) == 9 and len(sol) == 9, "Ambas as grades devem ter 9 linhas."
    for row in puzzle:
        assert len(row) == 9, "Cada linha do puzzle deve ter 9 colunas."
    for row in sol:
        assert len(row) == 9, "Cada linha da solução deve ter 9 colunas."

    # Verifica se o puzzle tem pelo menos 17 células preenchidas (pois são necessárias pelo menos 17 dicas)
    filled_cells = sum(1 for row in puzzle for cell in row if cell != ' ')
    assert filled_cells >= 17, "O puzzle deve ter pelo menos 17 células preenchidas."

def test_format(capsys):
    """
    Testa se a função format() imprime a grade no formato esperado.
    """
    puzzle = [
        ['1', ' ', '3', ' ', '5', ' ', '7', ' ', '9'],
        [' ', '2', ' ', '4', ' ', '6', ' ', '8', ' '],
        ['3', ' ', '5', ' ', '7', ' ', '9', ' ', '1'],
        [' ', '4', ' ', '6', ' ', '8', ' ', '1', ' '],
        ['5', ' ', '7', ' ', '9', ' ', '1', ' ', '3'],
        [' ', '6', ' ', '8', ' ', '1', ' ', '3', ' '],
        ['7', ' ', '9', ' ', '1', ' ', '3', ' ', '5'],
        [' ', '8', ' ', '1', ' ', '3', ' ', '5', ' '],
        ['9', ' ', '1', ' ', '3', ' ', '5', ' ', '7']
    ]
    format(puzzle)
    captured = capsys.readouterr()
    output = captured.out
    assert "╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗" in output, "Formatação incorreta do topo da grade."
    assert "╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝" in output, "Formatação incorreta da base da grade."
    assert "1" in output, "Conteúdo da grade não foi impresso corretamente."