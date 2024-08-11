from typing import List, Set

from core.model.board import SudokuBoard, subgrid_of_board, board_has_empty_cells


def has_valid_nums(row):
    """ Returns True if the row has no duplicate numbers (except 0) """
    nums = set()
    for num in row:
        if num == 0:
            continue
        if num in nums:
            return False
        nums.add(num)
    return True


def check_board(board: SudokuBoard) -> List[str]:
    problems = []

    for i, row in enumerate(board):
        if not has_valid_nums(row):
            problems.append(f"Row {i} has duplicates: {row}")

    for j, column in enumerate(board.T):
        if not has_valid_nums(column):
            problems.append(f"Column {j} has duplicates: {column}")

    for i in range(3):
        for j in range(3):
            subgrid = subgrid_of_board(board, i, j)
            if not has_valid_nums(subgrid.flatten()):
                problems.append(f"Subgrid {i}, {j} has duplicates:\n{subgrid}")

    return problems


def is_completed(board: SudokuBoard) -> bool:
    return not board_has_empty_cells(board)


def is_solved(board: SudokuBoard) -> bool:
    return is_completed(board) and len(check_board(board)) == 0
