from typing import Set, Iterable

import numpy as np

SudokuBoard = np.ndarray


def subgrid_of_board(board: SudokuBoard, i: int, j: int) -> np.ndarray:
    return board[i * 3:(i + 1) * 3, j * 3:(j + 1) * 3]


def subgrids_of_board(board: SudokuBoard) -> Iterable[np.ndarray]:
    return (subgrid_of_board(board, i, j) for i in range(3) for j in range(3))


def numbers_in_row(board: SudokuBoard, i: int) -> Set[int]:
    return set(board[i, :].flatten())


def numbers_in_column(board: SudokuBoard, j: int) -> Set[int]:
    return set(board[:, j].flatten())


def numbers_in_subgrid(board: SudokuBoard, i: int, j: int) -> Set[int]:
    return set(subgrid_of_board(board, i, j).flatten())


ZERO_TO_NINE = range(1, 10)


def find_missing_numbers(nums: np.ndarray) -> Set[int]:
    return set(ZERO_TO_NINE) - set(nums)


def make_empty_board():
    return np.zeros((9, 9), dtype=int)


def board_has_empty_cells(board: SudokuBoard) -> bool:
    return 0 in board
