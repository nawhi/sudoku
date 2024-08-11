import unittest

from core.parser import parse_board
from core.model.board import make_empty_board
from core.strategies.elimination import single_cell_elimination, subgrid_elimination, column_elimination, \
    row_elimination
from test.util import SudokuTestCase


class TestSingleCellElimination(SudokuTestCase):
    def test_does_nothing_if_nothing_to_do(self):
        empty = make_empty_board()
        after = single_cell_elimination(empty)
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
        after = single_cell_elimination(before)
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
        after = single_cell_elimination(before)
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


class TestSubgridElimination(SudokuTestCase):
    def test_adds_number_in_top_left(self):
        before = parse_board("""
            ┌───────┬───────┬───────┐
            │ 3 4 2 │ . . . │ . . . │
            │ 6 . 5 │ . 7 . │ . . . │
            │ . . . │ . . . │ . . . │
            ├───────┼───────┼───────┤
            │ . . . │ . . . │ . . . │
            │ . . . │ . . . │ . . . │
            │ . . 7 │ . . . │ . . . │
            ├───────┼───────┼───────┤
            │ . . . │ . . . │ . . . │
            │ . . . │ . . . │ . . . │
            │ 7 . . │ . . . │ . . . │
            └───────┴───────┴───────┘
        """)

        after = subgrid_elimination(before)

        expected = parse_board("""
            ┌───────┬───────┬───────┐
            │ 3 4 2 │ . . . │ . . . │
            │ 6 . 5 │ . 7 . │ . . . │
            │ . 7 . │ . . . │ . . . │
            ├───────┼───────┼───────┤
            │ . . . │ . . . │ . . . │
            │ . . . │ . . . │ . . . │
            │ . . 7 │ . . . │ . . . │
            ├───────┼───────┼───────┤
            │ . . . │ . . . │ . . . │
            │ . . . │ . . . │ . . . │
            │ 7 . . │ . . . │ . . . │
            └───────┴───────┴───────┘
        """)

        self.assertBoardsEqual(after, expected)

    def test_handles_real_world_example(self):
        before = parse_board("""
            ┌───────┬───────┬───────┐
            │ . 9 . │ . 7 . │ 3 4 2 │
            │ 7 . . │ . . 2 │ 6 . 5 │
            │ . . . │ . . . │ . . . │
            ├───────┼───────┼───────┤
            │ . . 4 │ 6 . . │ . . 8 │
            │ . 5 6 │ . . 4 │ . . . │
            │ . . 2 │ . 5 . │ . . 7 │
            ├───────┼───────┼───────┤
            │ . . . │ . . . │ 9 2 3 │
            │ . 2 . │ . . . │ . 5 . │
            │ 3 . 8 │ . . . │ 7 . . │
            └───────┴───────┴───────┘
        """)

        after = subgrid_elimination(before)

        expected = parse_board("""
            ┌───────┬───────┬───────┐
            │ . 9 . │ . 7 . │ 3 4 2 │
            │ 7 . . │ . . 2 │ 6 . 5 │
            │ 2 . . │ . . . │ . 7 . │
            ├───────┼───────┼───────┤
            │ . 7 4 │ 6 . . │ 5 . 8 │
            │ . 5 6 │ 7 . 4 │ . . . │
            │ . . 2 │ . 5 . │ 4 6 7 │
            ├───────┼───────┼───────┤
            │ . . . │ . . . │ 9 2 3 │
            │ . 2 . │ . . . │ 8 5 . │
            │ 3 . 8 │ . . . │ 7 . . │
            └───────┴───────┴───────┘
        """)
        self.assertBoardsEqual(after, expected)


@unittest.skip("WIP")
class TestColumnElimination(SudokuTestCase):
    def test_adds_number_to_column(self):
        before = parse_board("""
            ┌───────┬───────┬───────┐
            │ . 9 . │ . . . │ . . . │
            │ . . . │ . . . │ . 8 . │
            │ . . . │ . . . │ . . . │
            ├───────┼───────┼───────┤
            │ . 7 . │ . . . │ . . . │
            │ . 5 . │ . . . │ . . . │
            │ . 3 . │ . . . │ . . . │
            ├───────┼───────┼───────┤
            │ . . . │ . . . │ . . . │
            │ . 2 . │ . . . │ . . . │
            │ . . 8 │ . . . │ . . . │
            └───────┴───────┴───────┘
        """)

        after = column_elimination(before)

        expected = parse_board("""
            ┌───────┬───────┬───────┐
            │ . 9 . │ . . . │ . . . │
            │ . . . │ . . . │ . 8 . │
            │ . 8 . │ . . . │ . . . │
            ├───────┼───────┼───────┤
            │ . 7 . │ . . . │ . . . │
            │ . 5 . │ . . . │ . . . │
            │ . 3 . │ . . . │ . . . │
            ├───────┼───────┼───────┤
            │ . . . │ . . . │ . . . │
            │ . 2 . │ . . . │ . . . │
            │ . . 8 │ . . . │ . . . │
            └───────┴───────┴───────┘
        """)
        self.assertBoardsEqual(after, expected)


@unittest.skip("WIP")
class TestRowElimination(SudokuTestCase):
    def test_adds_number_to_row(self):
        before = parse_board("""
            ┌───────┬───────┬───────┐
            │ . . . │ . . . │ . . 8 │
            │ 9 . . │ 7 5 3 │ . 2 . │
            │ . . . │ . . . │ . . . │
            ├───────┼───────┼───────┤
            │ . . . │ . . . │ . . . │
            │ . . . │ . . . │ . . . │
            │ . . . │ . . . │ . . . │
            ├───────┼───────┼───────┤
            │ . . . │ . . . │ . . . │
            │ . 8 . │ . . . │ . . . │
            │ . . . │ . . . │ . . . │
            └───────┴───────┴───────┘
        """)

        after = row_elimination(before)

        expected = parse_board("""
            ┌───────┬───────┬───────┐
            │ . . . │ . . . │ . . 8 │
            │ 9 . 8 │ 7 5 3 │ . 2 . │
            │ . . . │ . . . │ . . . │
            ├───────┼───────┼───────┤
            │ . . . │ . . . │ . . . │
            │ . . . │ . . . │ . . . │
            │ . . . │ . . . │ . . . │
            ├───────┼───────┼───────┤
            │ . . . │ . . . │ . . . │
            │ . 8 . │ . . . │ . . . │
            │ . . . │ . . . │ . . . │
            └───────┴───────┴───────┘
        """)
        self.assertBoardsEqual(after, expected)

    def test_does_not_result_in_invalid_board(self):
        board = parse_board("""
            ┌───────┬───────┬───────┐
            │ . 9 . │ . 7 . │ 3 4 2 │
            │ 7 . . │ . . 2 │ 6 . 5 │
            │ 2 . . │ . . . │ . 7 . │
            ├───────┼───────┼───────┤
            │ . . 4 │ 6 . . │ 5 . 8 │
            │ . 5 6 │ . . 4 │ . . 9 │
            │ . . 2 │ . 5 . │ 4 6 7 │
            ├───────┼───────┼───────┤
            │ . 7 . │ . . . │ 9 2 3 │
            │ . 2 9 │ . . . │ 8 5 . │
            │ 3 . 8 │ . . . │ 7 . . │
            └───────┴───────┴───────┘
        """)

        after = column_elimination(board.copy())
        self.assertBoardsEqual(after, board)
