from core.parser import parse_board
from core.model.board import make_empty_board
from core.strategies.elimination import row_col_subgrid_elimination
from test.util import SudokuTestCase


class TestElimination(SudokuTestCase):
    def test_does_nothing_if_nothing_to_do(self):
        empty = make_empty_board()
        after = row_col_subgrid_elimination(empty)
        self.assertBoardsEqual(empty, after)

    def test_fills_cell_using_row_and_column(self):
        before = parse_board("""
            ┌───────┬───────┬───────┐
            │ 1 2 3 │ 4 5 6 │ 7 . . │
            │ . . . │ . . . │ . . . │
            │ . . . │ . . . │ . . . │
            ├───────┼───────┼───────┤
            │ . . . │ . . . │ . . 9 │
            │ . . . │ . . . │ . . . │
            │ . . . │ . . . │ . . . │
            ├───────┼───────┼───────┤
            │ . . . │ . . . │ . . . │
            │ . . . │ . . . │ . . . │
            │ . . . │ . . . │ . . . │
            └───────┴───────┴───────┘
        """)
        after = row_col_subgrid_elimination(before)
        expected = parse_board("""
            ┌───────┬───────┬───────┐
            │ 1 2 3 │ 4 5 6 │ 7 . 8 │
            │ . . . │ . . . │ . . . │
            │ . . . │ . . . │ . . . │
            ├───────┼───────┼───────┤
            │ . . . │ . . . │ . . 9 │
            │ . . . │ . . . │ . . . │
            │ . . . │ . . . │ . . . │
            ├───────┼───────┼───────┤
            │ . . . │ . . . │ . . . │
            │ . . . │ . . . │ . . . │
            │ . . . │ . . . │ . . . │
            └───────┴───────┴───────┘
        """)

        self.assertBoardsEqual(after, expected)

    def test_fills_cell_using_row_and_subgrid(self):
        before = parse_board("""
            ┌───────┬───────┬───────┐
            │ . . . │ . . . │ . . . │
            │ . . . │ . . . │ . . . │
            │ . . . │ . . . │ . . . │
            ├───────┼───────┼───────┤
            │ . . . │ 7 . 8 │ . . . │
            │ . . . │ . . . │ 1 2 3 │
            │ . . . │ . . . │ . . . │
            ├───────┼───────┼───────┤
            │ . . . │ . 4 . │ . . . │
            │ . . . │ . 5 . │ . . . │
            │ . . . │ . 6 . │ . . . │
            └───────┴───────┴───────┘
        """)
        after = row_col_subgrid_elimination(before)
        expected = parse_board("""
            ┌───────┬───────┬───────┐
            │ . . . │ . . . │ . . . │
            │ . . . │ . . . │ . . . │
            │ . . . │ . . . │ . . . │
            ├───────┼───────┼───────┤
            │ . . . │ 7 . 8 │ . . . │
            │ . . . │ . 9 . │ 1 2 3 │
            │ . . . │ . . . │ . . . │
            ├───────┼───────┼───────┤
            │ . . . │ . 4 . │ . . . │
            │ . . . │ . 5 . │ . . . │
            │ . . . │ . 6 . │ . . . │
            └───────┴───────┴───────┘
        """)

        self.assertBoardsEqual(after, expected)
