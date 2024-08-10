from core.parser import parse_board
from core.printer import board_as_string
from test.util import SudokuTestCase
from test.examples import PUZZLE_EASY

PUZZLE_EASY_INDENTED = """
>>>┌───────┬───────┬───────┐
>>>│ . . 6 │ 8 7 1 │ . . 3 │
>>>│ . 7 3 │ . 5 6 │ 1 9 . │
>>>│ . . . │ 3 4 9 │ . 2 7 │
>>>├───────┼───────┼───────┤
>>>│ 3 4 2 │ . . . │ . 8 . │
>>>│ . 6 . │ . 2 . │ . . . │
>>>│ . . . │ . . 3 │ . 5 2 │
>>>├───────┼───────┼───────┤
>>>│ . 1 . │ 7 . 4 │ 8 . . │
>>>│ 7 . . │ 5 9 8 │ 2 6 1 │
>>>│ . . 5 │ . . . │ 9 . . │
>>>└───────┴───────┴───────┘
"""


class TestPrinter(SudokuTestCase):
    def test_print_board(self):
        printed = board_as_string(parse_board(PUZZLE_EASY))
        self.assertEqual(PUZZLE_EASY.strip(), printed)

    def test_indented_print(self):
        printed = board_as_string(parse_board(PUZZLE_EASY), line_prefix=">>>")
        self.assertEqual(PUZZLE_EASY_INDENTED.strip(), printed)
