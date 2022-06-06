def drawboard(board):
    print(" 1 2 3")
    print("1" + board[0][0].mark + "|" + board[1][0].mark + "|" + board[2][0].mark)
    print(" _____")
    print("2" + board[0][1].mark + "|" + board[1][1].mark + "|" + board[2][1].mark)
    print(" _____")
    print("3" + board[0][2].mark + "|" + board[1][2].mark + "|" + board[2][2].mark)