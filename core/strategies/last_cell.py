def last_cell_in_column_strategy(board):
    for column in board.transpose():
        missing = set(range(1, 10)) - set(column)
        if len(missing) == 1:
            column[column == 0] = missing.pop()
    return board


def last_cell_in_row_strategy(board):
    for row in board:
        missing = set(range(1, 10)) - set(row)
        if len(missing) == 1:
            row[row == 0] = missing.pop()
    return board
