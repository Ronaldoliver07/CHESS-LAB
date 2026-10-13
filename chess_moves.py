import numpy as np
from chess_board import board, black_piece, white_piece, board_cords


class chessmoves:

    def black_move():

        move = input("INPUT BLACK MOVES: ")

        ''' Locate initial pos of piece '''

        p_name = move[0]
        p_id = black_piece[p_name]
        
        p_before_loc = np.where(board == p_id)
        p_before_loc = str(p_before_loc)
        col=int(p_before_loc[20])
        row=int(p_before_loc[8])
        p_before_loc = [row , col]


        ''' Locate final pos of piece '''

        p_text_col = move[1]
        p_final_row = move[2]
        p_final_col = board_cords[p_text_col]

        p_final_row = int(p_final_row) - 1
        p_final_col = p_final_col - 1

        p_after_loc = [p_final_row , p_final_col]

        print("black moves")
        print (p_before_loc) 
        print(p_after_loc )
        



    def white_move():

        move = input("INPUT WHITE MOVES: ")

        ''' Locate initial pos of piece '''

        p_name = move[0]
        p_id = white_piece[p_name]
        
        p_before_loc = np.where(board == p_id)
        p_before_loc = str(p_before_loc)
        col=int(p_before_loc[20])
        row=int(p_before_loc[8])
        p_before_loc = [row , col]


        ''' Locate final pos of piece '''

        p_text_col = move[1]
        p_final_row = move[2]


        p_final_col = board_cords[p_text_col]

        p_final_row = int(p_final_row) - 1
        p_final_col = p_final_col - 1

        p_after_loc = [p_final_row , p_final_col]

        print("white moves")
        print (p_before_loc) 
        print(p_after_loc )
    
