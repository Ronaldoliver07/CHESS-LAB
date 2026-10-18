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

    print(board)
    board = rules.w_update_board(white_move, board)
    print(board)





    black_move = chessmoves.black_move()

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

    print(board)
    board = rules.b_update_board(black_move, board)
    print(board)
    