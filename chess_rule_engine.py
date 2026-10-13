import numpy as np
from chess_moves import chessmoves

'''rule engine'''

class rules:

    def boardrules(position):
        [p,[a,b],[x,y]] = position

        space = True

        if not (0 <= a < 8):
            print("game currepted")
            space =  False
        if not (0 <= b < 8):
            print("game currepted")
            space =  False
        if not (0 <= x < 8):
            print("Enter right values")
            space =  False
        if not (0 <= y < 8):
            print("enter right values")
            space = False

        if p == "k":
            if max(abs(a - x), abs(b - y)) == 1 and space:
                print ("king works")
                return True

            else:
                return False

     


while True:
    white_move = chessmoves.white_move()

    check= rules.boardrules(white_move)

    if check == False:
        break



    black_move = chessmoves.black_move()

    check= rules.boardrules(black_move)
    
    if check == False:
        break
    
    


