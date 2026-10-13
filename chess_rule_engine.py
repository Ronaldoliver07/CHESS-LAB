import numpy as np
from chess_moves import chessmoves

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

    def k_rules(position):

        [p,[a,b],[x,y]] = position


        if max(abs(a - x), abs(b - y)) == 1 :
            return True

        else:
            print("invalid king move")
            return False

    def R_rules(position):

        [p,[a,b],[x,y]] = position

        if (abs(a - x) == 0) or (abs(b - y) == 0) :
            return True

        else:
            print("invalid Rook move")
            return False



while True:
    white_move = chessmoves.white_move()

    board_check= rules.boardrules(white_move)
    if board_check == False:
        break

    if white_move[0] == "k":
        piece_check= rules.k_rules(white_move)

        if piece_check == False:
            break

    if white_move[0] == "r" or "R":
        piece_check= rules.R_rules(white_move)

        if piece_check == False:
            break

    








    black_move = chessmoves.black_move()


    
    


