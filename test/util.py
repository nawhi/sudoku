import re
import unittest
from typing import List

import numpy as np

from core.model.board import make_empty_board
from core.printer import board_as_string


class SudokuTestCase(unittest.TestCase):
    def assertBoardsEqual(self, board: np.ndarray, expected: np.ndarray):
        self.assertEqual(board_as_string(board), board_as_string(expected))


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
