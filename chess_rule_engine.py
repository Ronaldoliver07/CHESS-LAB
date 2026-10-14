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
            print("invalid piece move")
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

    if (white_move[0] == "r") or (white_move[0] == "R") :
        piece_check= rules.R_rules(white_move)


        if piece_check == False:
            break

    if (white_move[0] == "b") or (white_move[0] == "B"):
        piece_check= rules.B_rules(white_move)

        if piece_check == False:
            break   


    if (white_move[0] == "n") or (white_move[0] == "N"):
        piece_check= rules.N_rules(white_move)

        if piece_check == False:
            break   


    if white_move[0] == " ":
        piece_check= rules.P_rules(white_move)

        if piece_check == False:
            break  

    if white_move[0] == "q":
        piece_check= rules.q_rules(white_move)

        if piece_check == False:
            break  



    black_move = chessmoves.black_move()

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

    if white_move[0] == "b" or "B":
        piece_check= rules.B_rules(white_move)

        if piece_check == False:
            break   


    if white_move[0] == "n" or "N":
        piece_check= rules.N_rules(white_move)

        if piece_check == False:
            break   


    if white_move[0] == " ":
        piece_check= rules.P_rules(white_move)

        if piece_check == False:
            break   

    if white_move[0] == "q":
        piece_check= rules.q_rules(white_move)

        if piece_check == False:
            break  

    
    


