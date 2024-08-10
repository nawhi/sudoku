from core.model.board import find_missing_numbers


def last_cell_in_column(board):
    for column in board.transpose():
        missing = set(range(1, 10)) - set(column)
        if len(missing) == 1:
            column[column == 0] = missing.pop()
    return board


def last_cell_in_row(board):
    for row in board:
        missing = set(range(1, 10)) - set(row)
        if len(missing) == 1:
            row[row == 0] = missing.pop()
    return board


def last_cell_in_subgrid(board):
    for i in range(3):
        for j in range(3):
            subgrid = board[i * 3:(i + 1) * 3, j * 3:(j + 1) * 3]
            nums = subgrid.flatten()
            missing = find_missing_numbers(nums)
            if len(missing) == 1:
                subgrid[subgrid == 0] = missing.pop()
    return board

