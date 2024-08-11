import numpy as np

from core.checker import is_solved
from core.model.board import SudokuBoard
from core.printer import board_as_string
from core.strategies.elimination import single_cell_elimination, subgrid_elimination
from core.strategies.last_cell import last_cell_in_row, last_cell_in_column, last_cell_in_subgrid

STRATEGIES = [
    last_cell_in_row,
    last_cell_in_column,
    last_cell_in_subgrid,
    single_cell_elimination,
    subgrid_elimination
]


def all_strategies_failed(board):
    message = f"""
    Cannot solve this board!
    Board state before failure:\n{board_as_string(board, line_prefix="    ")}
    All strategies tried:
    {", ".join(strategy.__name__ for strategy in STRATEGIES)}
    """
    raise NotImplementedError(message)


def solve(board: SudokuBoard) -> SudokuBoard:
    while True:
        board_before = board.copy()
        for strategy in STRATEGIES:
            try:
                board = strategy(board)
            except RuntimeError as err:
                print(f"Strategy {strategy.__name__} crashed with message: {err}")
                print(f"Board state before errored strategy:\n{board_as_string(board)}")
                raise err
        if np.array_equal(board, board_before):
            all_strategies_failed(board)
        if is_solved(board):
            return board
