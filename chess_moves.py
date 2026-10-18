
import numpy as np
from chess_board import board, black_piece, white_piece, board_cords


class chessmoves:

    def black_move(move):

        ''' Locate initial pos of piece '''

        p_name = move[0]
        p_id = black_piece[p_name]

        rows, cols = np.where(board == p_id)

        if len(rows) == 0:
            return None

        p_before_loc = [int(rows[0]), int(cols[0])]

        ''' Locate final pos of piece '''

        p_text_col = move[1]
        p_final_row = move[2]
        p_final_col = board_cords[p_text_col]

        p_final_row = int(p_final_row) - 1
        p_final_col = p_final_col - 1

        p_after_loc = [p_final_row, p_final_col]

        return [p_name, p_before_loc, p_after_loc]


    def white_move(move):

        ''' Locate initial pos of piece '''

        p_name = move[0]
        p_id = white_piece[p_name]

        rows, cols = np.where(board == p_id)

        if len(rows) == 0:
            return None

        p_before_loc = [int(rows[0]), int(cols[0])]

        ''' Locate final pos of piece '''

        p_text_col = move[1]
        p_final_row = move[2]
        p_final_col = board_cords[p_text_col]

        p_final_row = int(p_final_row) - 1
        p_final_col = p_final_col - 1

        p_after_loc = [p_final_row, p_final_col]

        return [p_name, p_before_loc, p_after_loc]
