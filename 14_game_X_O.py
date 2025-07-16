import random
size = 3
board = [[" " for i in range(size)] for j in range(size)]


def printBoard():
    row_counter = 0
    counter  = 0
    for row in board:
        row_counter += 1
        item_counter = 0
        for item in row:
            item_counter += 1
            print(" " + item + " " + (chr(9553) if item_counter < len(row) else ""),end="")
        print(end = "\t\t")
        item_counter = 0
        for item in range(len(row)):
            item_counter += 1
            counter+=1
            print(" " + str(counter) + " " + (chr(9553) if item_counter < len(row) else ""),end="")
        print()
        print(chr(9552)* (3 * item_counter + 2) if row_counter < len(board) else "", end= "\t\t")
        print(chr(9552)* (3 * item_counter + 2) if row_counter < len(board) else "")

def convertCoord(number):
    match number:
        case 1:
            return 0,0
        case 2:
            return 0,1
        case 3:
            return 0,2
        case 4:
            return 1,0
        case 5:
            return 1,1
        case 6:
            return 1,2
        case 7:
            return 2,0
        case 8:
            return 2,1
        case 9:
            return 2,2

def check(a,b,c):
    a_x, a_y = convertCoord(a)
    b_x, b_y = convertCoord(b)
    c_x, c_y = convertCoord(c)
    return board[a_x][a_y] == board[b_x][b_y] and board[b_x][b_y] == board[c_x][c_y]

def checkAll():
    if board[0][0] != " ":
        if check(1,2,3) or check(1,5,9) or check(1,4,7):
            return True
    if board[0][1] != " ":
        if check(2,5,8) :
            return True
    if board[0][2] != " ":
        if check(3,5,7) or check(3,6,9):
            return True
    if board[1][0] != " ":
        if check(4,5,6):
            return True
    if board[2][0] != " ":
        if check(7,8,9):
            return True

def start_game():
    user = "X"
    bot = "O"
    player = True if user == "X" else False
    printBoard()
    counter = 0
    while counter < 9:
        if player:
            choice = int(input("Enter number :: "))
            user_x, user_y  = convertCoord(choice)
            if board[user_x][user_y] == " ":
                board[user_x][user_y] = user
                if checkAll():
                    print("Congratulation!!! Player X")
                    break
                player = False
                counter+=1
        else:
            bot_rnd = random.randint(1,9)
            bot_x, bot_y  = convertCoord(bot_rnd)
            if board[bot_x][bot_y] == " ":
                board[bot_x][bot_y] = bot
                if checkAll():
                    print("Sorry!!! You Loser! Win O")
                    break
                player = True
                counter+=1

        printBoard()
    else:
        print("Draw")
    printBoard()

start_game()


