from typing import Set

import numpy as np

SudokuBoard = np.ndarray


def subgrid_of_board(board: SudokuBoard, i: int, j: int) -> np.ndarray:
    return board[i * 3:(i + 1) * 3, j * 3:(j + 1) * 3]


ZERO_TO_NINE = range(1, 10)


def find_missing_numbers(nums: np.ndarray) -> Set[int]:
    return set(ZERO_TO_NINE) - set(nums)
