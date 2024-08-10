import numpy as np

from core.model.board import SudokuBoard
from core.checker import is_solved
from core.printer import board_as_string
from core.strategies.elimination import row_col_subgrid_elimination
from core.strategies.last_cell import last_cell_in_row, last_cell_in_column, last_cell_in_subgrid

STRATEGIES = [
    last_cell_in_row,
    last_cell_in_column,
    last_cell_in_subgrid,
    row_col_subgrid_elimination
]


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
            print("No progress made!")
            print("Current board state:")
            print(board_as_string(board))
            raise NotImplementedError("Can't solve this board!")
        if is_solved(board):
            return board
