import re
import unittest
from typing import List

import numpy as np


EXAMPLE_BOARD = """
┌───────┬───────┬───────┐
│ . . 6 │ 8 7 1 │ . . 3 │
│ . 7 3 │ . 5 6 │ 1 9 . │
│ . . . │ 3 4 9 │ . 2 7 │
├───────┼───────┼───────┤
│ 3 4 2 │ . . . │ . 8 . │
│ . 6 . │ . 2 . │ . . . │
│ . . . │ . . 3 │ . 5 2 │
├───────┼───────┼───────┤
│ . 1 . │ 7 . 4 │ 8 . . │
│ 7 . . │ 5 9 8 │ 2 6 1 │
│ . . 5 │ . . . │ 9 . . │
└───────┴───────┴───────┘
"""

class SudokuTestCase(unittest.TestCase):
    def assertBoardsEqual(self, board: np.ndarray, expected: np.ndarray):
        self.assertEqual(board.tolist(), expected.tolist())


def make_empty_board():
    return np.zeros((9, 9), dtype=int)


def board_of_rows(raw_rows: List[str]):
    board = make_empty_board()
    for i, raw_row in enumerate(raw_rows):
        parsed_row = re.compile(r"[0-9.]", re.MULTILINE).findall(raw_row)
        if len(parsed_row) != 9:
            raise ValueError(f"Invalid row: expected to find 9 numbers, got {len(parsed_row)}")
        board[i] = [int(n) if n != "." else 0 for n in parsed_row]
    return board


def board_of_first_row(raw_row: str):
    return board_of_rows([raw_row])
