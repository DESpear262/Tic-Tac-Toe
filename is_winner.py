def is_winner(board):
    winner=False
    if board[0][0].mark == board[0][1].mark and board[0][0].mark == board[0][2].mark and board[0][0].mark != " ":   #top row
        winner=True
    elif board[0][1].mark == board[1][1].mark and board[0][1].mark == board[2][1].mark and board[0][1].mark != " ": #mid row
        winner=True
    elif board[2][0].mark == board[2][1].mark and board[2][0].mark == board[2][2].mark and board[2][0].mark != " ": #bot row
        winner=True
    elif board[0][2].mark == board[1][2].mark and board[0][2].mark == board[2][2].mark and board[0][2].mark != " ": #rt col
        winner=True
    elif board[0][0].mark == board[1][0].mark and board[0][0].mark == board[2][0].mark and board[0][0].mark != " ": #lt col
           winner=True
    elif board[1][0].mark == board[1][1].mark and board[1][0].mark == board[1][2].mark and board[1][0].mark != " ": #mid col
           winner=True
    elif board[0][0].mark == board[1][1].mark and board[0][0].mark == board[2][2].mark and board[0][0].mark != " ": #diag 1
           winner=True
    elif board[2][0].mark == board[1][1].mark and board[2][0].mark == board[0][2].mark and board[2][0].mark != " ": #diag 2
        winner=True
    return winner