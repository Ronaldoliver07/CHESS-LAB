import numpy as np


def collision_capture_rule(board: np.ndarray, move: list) -> bool:

    _, [from_row, from_col], [to_row, to_col] = move

    if not (
        0 <= from_row < board.shape[0]
        and 0 <= from_col < board.shape[1]
        and 0 <= to_row < board.shape[0]
        and 0 <= to_col < board.shape[1]
    ):
        return False

    moving_piece = board[from_row, from_col]
    target_piece = board[to_row, to_col]

    if moving_piece == 0:
        return False

    if target_piece != 0 and (moving_piece > 0) == (target_piece > 0):
        return False

    board[to_row, to_col] = moving_piece
    board[from_row, from_col] = 0
    return True
