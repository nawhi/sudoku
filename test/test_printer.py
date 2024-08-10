from core.parser import parse_board
from core.printer import board_as_string
from test.util import SudokuTestCase, EXAMPLE_BOARD


class TestPrinter(SudokuTestCase):
    def test_print_board(self):
        printed = board_as_string(parse_board(EXAMPLE_BOARD))
        self.assertEqual(EXAMPLE_BOARD.strip(), printed)
