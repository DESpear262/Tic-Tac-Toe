This project is basically a tutoring tool for teaching Python. Over the course of the tutorial, the student will recreate this program with my guidance, including learning about loops, conditional statements, lists, file I/O, and general software engineering reasoning skills.

main.py is the main file which instantiates the players, encodes the core gameplay loop, asks the player if they want to play again after the game concludes, and updates the scoreboard dictionary, before saving it to an external .txt file in readable format.

drawboard.py prints an ASCII tic tac toe board in the current board state to the terminal

is_stalemate.py checks whether the game has ended in a stalemate by checking if the round currently ending is the 9th. Since this function is called in a conditional statement if and only if is_winner returns false, there is no need to check in this method itself whether the game was won on the final round.

is_winner.py checks all possible winning board positions, and returns true if one exists, else return false.

makeboard.py creates a list of lists of instances of the square class, to be used as the game board

scoreboard.py is a dictionary where player names are paired with their lifetime scores.

square.py defines the square class, which is used to store whether a square has been marked and which player marked it.

turn.py encodes a turn of the game, including checking the validity of the input (input coordinates are on the board, the square indicated is unmarked, etc.).
