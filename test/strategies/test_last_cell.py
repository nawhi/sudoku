import unittest

from core.parser import parse_board
from core.strategies.last_cell import last_cell_in_row_strategy, last_cell_in_column_strategy
from test.util import SudokuTestCase, board_of_first_row, board_of_rows


class TestLastCellInRowStrategy(SudokuTestCase):
    def test_fills_one_last_cell(self):
        before = board_of_first_row("123|456|78.")
        after = last_cell_in_row_strategy(before)
        self.assertBoardsEqual(after, board_of_first_row("123|456|789"))

    def test_fills_many_last_cells(self):
        before = board_of_rows(["123|456|78.", "123|456|78.", "123|456|78."])
        after = last_cell_in_row_strategy(before)
        expected = board_of_rows(["123|456|789", "123|456|789", "123|456|789"])
        self.assertBoardsEqual(after, expected)

    def test_does_nothing_if_no_last_cell(self):
        before = board_of_first_row("123|456|789")
        after = last_cell_in_row_strategy(before)
        self.assertBoardsEqual(after, board_of_first_row("123|456|789"))


class TestLastCellInColumnStrategy(SudokuTestCase):
    def test_fills_one_last_cell(self):
        before = parse_board("""
            ┌───────┬───────┬───────┐
            │ 8 . . │ . . . │ . . . │
            │ 7 . . │ . . . │ . . . │
            │ 6 . . │ . . . │ . . . │
            ├───────┼───────┼───────┤
            │ 4 . . │ . . . │ . . . │
            │ . . . │ . . . │ . . . │
            │ 5 . . │ . . . │ . . . │
            ├───────┼───────┼───────┤
            │ 1 . . │ . . . │ . . . │
            │ 3 . . │ . . . │ . . . │
            │ 2 . . │ . . . │ . . . │
            └───────┴───────┴───────┘
        """)
        after = last_cell_in_column_strategy(before)
        self.assertBoardsEqual(after, parse_board("""
            ┌───────┬───────┬───────┐
            │ 8 . . │ . . . │ . . . │
            │ 7 . . │ . . . │ . . . │
            │ 6 . . │ . . . │ . . . │
            ├───────┼───────┼───────┤
            │ 4 . . │ . . . │ . . . │
            │ 9 . . │ . . . │ . . . │
            │ 5 . . │ . . . │ . . . │
            ├───────┼───────┼───────┤
            │ 1 . . │ . . . │ . . . │
            │ 3 . . │ . . . │ . . . │
            │ 2 . . │ . . . │ . . . │
            └───────┴───────┴───────┘
        """))

    def test_fills_many_last_cells(self):
        before = parse_board("""
            ┌───────┬───────┬───────┐
            │ 8 . . │ 1 . . │ . . . │
            │ 7 . . │ 2 . . │ . . . │
            │ 6 . . │ 3 . . │ . . . │
            ├───────┼───────┼───────┤
            │ 4 . . │ 5 . . │ . . . │
            │ . . . │ 6 . . │ . . . │
            │ 5 . . │ 7 . . │ . . . │
            ├───────┼───────┼───────┤
            │ 1 . . │ 8 . . │ . . . │
            │ 3 . . │ 9 . . │ . . . │
            │ 2 . . │ . . . │ . . . │
            └───────┴───────┴───────┘
        """)
        after = last_cell_in_column_strategy(before)
        self.assertBoardsEqual(after, parse_board("""
            ┌───────┬───────┬───────┐
            │ 8 . . │ 1 . . │ . . . │
            │ 7 . . │ 2 . . │ . . . │
            │ 6 . . │ 3 . . │ . . . │
            ├───────┼───────┼───────┤
            │ 4 . . │ 5 . . │ . . . │
            │ 9 . . │ 6 . . │ . . . │
            │ 5 . . │ 7 . . │ . . . │
            ├───────┼───────┼───────┤
            │ 1 . . │ 8 . . │ . . . │
            │ 3 . . │ 9 . . │ . . . │
            │ 2 . . │ 4 . . │ . . . │
            └───────┴───────┴───────┘
        """))


if __name__ == '__main__':
    unittest.main()
