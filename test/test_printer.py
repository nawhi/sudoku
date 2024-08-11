from core.parser import parse_board
from core.printer import board_as_string
from test.examples import PUZZLE_EASY
from test.util import SudokuTestCase


class TestPrinter(SudokuTestCase):
    def test_print_board(self):
        printed = board_as_string(parse_board(PUZZLE_EASY))
        self.assertEqual(PUZZLE_EASY.strip(), printed)
