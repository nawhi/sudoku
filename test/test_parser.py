import unittest

import numpy as np

from core.parser import parse_board

BOARD_AS_STRING = """
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

EXPECTED = np.array([
    [0, 0, 6, 8, 7, 1, 0, 0, 3],
    [0, 7, 3, 0, 5, 6, 1, 9, 0],
    [0, 0, 0, 3, 4, 9, 0, 2, 7],
    [3, 4, 2, 0, 0, 0, 0, 8, 0],
    [0, 6, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 5, 2],
    [0, 1, 0, 7, 0, 4, 8, 0, 0],
    [7, 0, 0, 5, 9, 8, 2, 6, 1],
    [0, 0, 5, 0, 0, 0, 9, 0, 0]
])


class TestParser(unittest.TestCase):
    def test_parse_board(self):
        board = parse_board(BOARD_AS_STRING)
        self.assertTrue(np.array_equal(board, EXPECTED))
