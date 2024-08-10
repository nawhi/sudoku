import numpy as np

from core.model.board import SudokuBoard, subgrid_of_board


def row_col_subgrid_elimination(board: SudokuBoard) -> SudokuBoard:
    """
    By elimination of possibilities based on the row, column and subgrid
    of a cell, fill in its value if there is only one possibility.

    This may write zeroes which is technically
    redundant but within the contract (if inefficient)
    """
    it = np.nditer(board, flags=['multi_index'])
    for val in it:
        if val != 0:
            continue
        x, y = it.multi_index
        candidates = set(range(1, 10))

        row = board[x, :]
        candidates -= set(row)

        if len(candidates) == 1:
            board[x, y] = candidates.pop()
            continue

        col = board[:, y]
        candidates -= set(col)

        if len(candidates) == 1:
            board[x, y] = candidates.pop()
            continue

        subgrid = subgrid_of_board(board, x // 3, y // 3)
        candidates -= set(subgrid.flatten())

        if len(candidates) == 1:
            board[x, y] = candidates.pop()
            continue

    return board
