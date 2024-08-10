from core.model.board import find_missing_numbers, SudokuBoard, subgrid_of_board


def last_cell_in_column(board: SudokuBoard) -> SudokuBoard:
    """ Where possible, fill in the last missing cell in any columns """
    for column in board.transpose():
        missing = set(range(1, 10)) - set(column)
        if len(missing) == 1:
            column[column == 0] = missing.pop()
    return board


def last_cell_in_row(board: SudokuBoard) -> SudokuBoard:
    """ Where possible, fill in the last missing cell in any row """
    for row in board:
        missing = set(range(1, 10)) - set(row)
        if len(missing) == 1:
            row[row == 0] = missing.pop()
    return board


def last_cell_in_subgrid(board: SudokuBoard) -> SudokuBoard:
    """ Where possible, fill in the last missing cell in any subgrid """
    for i in range(3):
        for j in range(3):
            subgrid = subgrid_of_board(board, i, j)
            nums = subgrid.flatten()
            missing = find_missing_numbers(nums)
            if len(missing) == 1:
                subgrid[subgrid == 0] = missing.pop()
    return board

