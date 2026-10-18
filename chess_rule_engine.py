import numpy as np
from chess_moves import chessmoves
from chess_board import board , white_piece , black_piece

'''rule engine'''

class rules:

    def boardrules(position):
        [p,[a,b],[x,y]] = position


        if not (0 <= a < 8):
            print("game currepted")
            return  False
        if not (0 <= b < 8):
            print("game currepted")
            return False
        if not (0 <= x < 8):
            print("Enter right values")
            return  False
        if not (0 <= y < 8):
            print("enter right values")
            return False

        else:
            return True

    def k_rules(position):

        [p,[a,b],[x,y]] = position


        if max(abs(a - x), abs(b - y)) == 1 :
            return True

        else:
            print("invalid king move")
            return False

    def R_rules(position):

        [p,[a,b],[x,y]] = position

        if ((abs(a - x) == 0) or (abs(b - y) == 0)) and (abs(a - x)  !=  abs(b - y)) :
            return True

        else:
            print("invalid Rook move")
            return False

    def B_rules(position):

        [p,[a,b],[x,y]] = position

        if ((abs(a - x) != 0) and (abs(b - y) != 0)) and (abs(a - x)  == abs(b - y)):
            return True

        else:
            print("invalid Bishop move")
            return False
        
    def N_rules(position):

        [p,[a,b],[x,y]] = position

        if ((abs(a - x) == 2) and (abs(b - y) == 1)) or ((abs(a - x) == 1) and (abs(b - y) == 2)):
            return True

        else:
            print("invalid Night move")
            return False

    def P_rules(position):

        [p,[a,b],[x,y]] = position

        if (abs(a - x) == 1) and (abs(b - y) == 0):
            return True

        else:
            print("invalid piece move")
            return False

    def q_rules(position):

        [p,[a,b],[x,y]] = position

        row_diff = abs(a - x)
        col_diff = abs(b - y)

        if (row_diff, col_diff) != (0, 0) and (
            row_diff == 0
            or col_diff == 0
            or row_diff == col_diff
              ):
                return True

        else:
            print("invalid Queen move")
            return False

    def w_update_board (position ,before_board):
        p, [a, b], [x, y] = position
        before_board[x, y] = white_piece[p]
        before_board[a, b] = 0

        return before_board

    def b_update_board (position ,before_board):
        p, [a, b], [x, y] = position
        before_board[x, y] = black_piece[p]
        before_board[a, b] = 0

        return before_board

