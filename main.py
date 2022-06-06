from makeboard import makeboard
from turn import *
from player import player
from is_winner import is_winner
from is_stalemate import is_stalemate
from drawboard import drawboard
from scoreboard import scoreboard_dict

play_again = ""


def update_scoreboard(win):
    if win in scoreboard_dict:
        scoreboard_dict[win] = scoreboard_dict[win] + 1
    else:
        scoreboard_dict[win] = 1
    

def save_scoreboard():
    f = open("tictactoe_Scoreboard.txt", "w")
    for x in scoreboard_dict:
        f.writelines(x + ": " + str(scoreboard_dict[x]) + "\n")
    f.close()

while play_again != "n":
    board = makeboard()

    p1=player(1, "", "")
    p2=player(2, "", "")

    p1.player_name=input("Player 1, what is your name?\t")
    p2.player_name=input("Player 2, what is your name?\t")

    #test code#
    update_scoreboard(p1.player_name)
    update_scoreboard(p1.player_name)
    update_scoreboard(p1.player_name)
    update_scoreboard(p2.player_name)
    save_scoreboard()
    #end test code#

    p1.team = input(p1.player_name + ", what team, would you like to be on? (Enter X or O):\t")
    while (p1.team != "X" and p1.team != "O"):
        if p1.team == "Simon is a loser":
            p1.team=input("No, u")
        else:
            p1.team = input("That is not a valid team! Enter an X or an O (use a capital letter O):\t")

    if p1.team == "X":
        p2.team = "O"
    else:
        p2.team = "X"

    rd_ct=0
    while not is_winner(board) and not is_stalemate(rd_ct):
        if rd_ct % 2 == 0:
            turn(board, p1.team)
        else:
            turn(board, p2.team)
        rd_ct = rd_ct + 1

    drawboard(board)
    rd_ct = rd_ct - 1
    if is_winner(board):
        if rd_ct % 2 == 0:
            print("Congratulations, " + p1.player_name + "! You win.")
#            with open(dict_scoreboard, "+") as sb:
#                if p1.player_name in dict_scoreboard:
#                    sb[p1.player_name] = sb[p1.player_name]+1
#                else:
#                    sb[p1.player_name] = 1
        else:
            print("Congratulations, " + p2.player_name + "! You win.")
            update_scoreboard(p2.player_name)
    else:
        print("It's a stalemate!")
    play_again = ""
    while play_again not in ["Y", "n"]:
        play_again = input("Would you like to play again? Y/n:\t")

save_scoreboard()
score = open("C:\\Users\\s94da\\Documents\\My Games\\Tic Tac Toe\\tictactoe_Scoreboard.txt", 'r')
for line in score:
    print(line)
score.close()

