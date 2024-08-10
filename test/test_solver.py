from core.checker import is_solved
from core.parser import parse_board
from core.solver import solve
from test.util import SudokuTestCase, EXAMPLE_BOARD


class TestSolver(SudokuTestCase):
    def test_acceptance_solves_easy_level_puzzle(self):
        puzzle = parse_board(EXAMPLE_BOARD)
        solved = solve(puzzle)
        self.assertTrue(is_solved(solved))
        print(solved)
