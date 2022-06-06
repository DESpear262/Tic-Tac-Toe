from drawboard import drawboard

def turn (board, team):
    drawboard(board)
    choice = input("Enter coordinates for the square you want to choose (input choice formatted \"[row] [column]\" counting from 1): ")
    error = is_valid(board, choice)

    while error != 0:
        drawboard(board)
        if error==1:
            choice=input("You dingus, those are bad coordinates! Put in numbers between 1 and 3:  ")
        elif error==2:
            choice=input("You dingus, that spot is already marked! Put your letter in an empty space:  ")
        elif error==3:
            choice=input("You dingus, that's outside of the board! Put numbers between 1 and 3:  ")
        error=is_valid(board, choice)
    board[(int(choice[-1]))-1][(int(choice[0]))-1].mark = team


def is_valid(board, choice):
    try:
        int(choice[0])
        int(choice[-1])
    except (ValueError, IndexError) as e:
        return 1
    else:
        try:
            if board[(int(choice[-1])-1)][(int(choice[0])-1)].mark != " ":
                return 2
        except IndexError:
            return 3
        else:
            return 0
