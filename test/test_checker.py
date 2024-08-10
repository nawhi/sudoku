from core.checker import is_solved
from core.parser import parse_board
from test.util import SudokuTestCase, board_of_first_row


class TestChecker(SudokuTestCase):
    def test_is_not_solved_if_board_has_blanks(self):
        self.assertFalse(is_solved(board_of_first_row('.........')))

    def test_is_solved_if_board_has_all_numbers(self):
        board = parse_board("""
            ┌───────┬───────┬───────┐
            │ 1 2 3 │ 4 5 6 │ 7 8 9 │
            │ 4 5 6 │ 7 8 9 │ 1 2 3 │
            │ 7 8 9 │ 1 2 3 │ 4 5 6 │
            ├───────┼───────┼───────┤
            │ 2 3 1 │ 5 6 4 │ 8 9 7 │
            │ 5 6 4 │ 8 9 7 │ 2 3 1 │
            │ 8 9 7 │ 2 3 1 │ 5 6 4 │
            ├───────┼───────┼───────┤
            │ 3 1 2 │ 6 4 5 │ 9 7 8 │
            │ 6 4 5 │ 9 7 8 │ 3 1 2 │
            │ 9 7 8 │ 3 1 2 │ 6 4 5 │
            └───────┴───────┴───────┘
        """)
        self.assertTrue(is_solved(board))

    def test_is_not_solved_if_duplicate_number_in_row(self):
        # note two nines in row 9
        board = parse_board("""
            ┌───────┬───────┬───────┐
            │ 1 2 3 │ 4 5 6 │ 7 8 9 │
            │ 4 5 6 │ 7 8 9 │ 1 2 3 │
            │ 7 8 9 │ 1 2 3 │ 4 5 6 │
            ├───────┼───────┼───────┤
            │ 2 3 1 │ 5 6 4 │ 8 9 7 │
            │ 5 6 4 │ 8 9 7 │ 2 3 1 │
            │ 8 9 7 │ 2 3 1 │ 5 6 4 │
            ├───────┼───────┼───────┤
            │ 3 1 2 │ 6 4 5 │ 9 7 8 │
            │ 6 4 5 │ 9 7 8 │ 3 1 2 │
            │ 9 7 8 │ 3 1 2 │ 6 4 9 │
            └───────┴───────┴───────┘
        """)

        self.assertFalse(is_solved(board))

    def test_is_not_solved_if_duplicate_number_in_column(self):
        # note two nines in column 1
        board = parse_board("""
            ┌───────┬───────┬───────┐
            │ 9 2 3 │ 4 5 6 │ 7 8 9 │
            │ 4 5 6 │ 7 8 9 │ 1 2 3 │
            │ 7 8 9 │ 1 2 3 │ 4 5 6 │
            ├───────┼───────┼───────┤
            │ 2 3 1 │ 5 6 4 │ 8 9 7 │
            │ 5 6 4 │ 8 9 7 │ 2 3 1 │
            │ 8 9 7 │ 2 3 1 │ 5 6 4 │
            ├───────┼───────┼───────┤
            │ 3 1 2 │ 6 4 5 │ 9 7 8 │
            │ 6 4 5 │ 9 7 8 │ 3 1 2 │
            │ 9 7 8 │ 3 1 2 │ 6 4 5 │
            └───────┴───────┴───────┘
        """)

        self.assertFalse(is_solved(board))

    def test_is_not_solved_if_duplicate_numbers_in_subgrid(self):
        # duplicate 3 in middle top and
        # duplicate 4 in middle bottom
        board = parse_board("""
            ┌───────┬───────┬───────┐
            │ 1 2 4 │ 3 5 6 │ 7 8 9 │
            │ 4 5 6 │ 7 8 9 │ 1 2 3 │
            │ 7 8 9 │ 1 2 3 │ 4 5 6 │
            ├───────┼───────┼───────┤
            │ 2 3 1 │ 5 6 4 │ 8 9 7 │
            │ 5 6 3 │ 8 9 7 │ 2 4 1 │
            │ 8 9 7 │ 2 3 1 │ 5 6 4 │
            ├───────┼───────┼───────┤
            │ 3 1 2 │ 6 4 5 │ 9 7 8 │
            │ 6 4 5 │ 9 7 8 │ 3 1 2 │
            │ 9 7 8 │ 4 1 2 │ 6 3 5 │
            └───────┴───────┴───────┘
        """)

        self.assertFalse(is_solved(board))
