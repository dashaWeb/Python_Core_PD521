import random
size = 3
board = [[" " for i in range(size)] for j in range(size)]


def printBoard():
    row_counter = 0
    counter = 0
    for row in board:
        row_counter += 1
        item_counter = 0
        for item in row:
            item_counter += 1
            print(" " + item + " " + (chr(9553)
                  if item_counter < len(row) else ""), end="")
        print(end="\t\t")
        item_counter = 0
        for item in range(len(row)):
            item_counter += 1
            counter += 1
            print(" " + str(counter) + " " + (chr(9553)
                  if item_counter < len(row) else ""), end="")
        print()
        print(chr(9552) * (3 * item_counter + 2)
              if row_counter < len(board) else "", end="\t\t")
        print(chr(9552) * (3 * item_counter + 2)
              if row_counter < len(board) else "")


def convertCoord(number):
    match number:
        case 1:
            return 0, 0
        case 2:
            return 0, 1
        case 3:
            return 0, 2
        case 4:
            return 1, 0
        case 5:
            return 1, 1
        case 6:
            return 1, 2
        case 7:
            return 2, 0
        case 8:
            return 2, 1
        case 9:
            return 2, 2


def check(a, b, c):
    a_x, a_y = convertCoord(a)
    b_x, b_y = convertCoord(b)
    c_x, c_y = convertCoord(c)
    return board[a_x][a_y] == board[b_x][b_y] and board[b_x][b_y] == board[c_x][c_y]


def reset():
    for i in range(3):
        for j in range(3):
            board[i][j] = " "
def checkAll():
    if board[0][0] != " ":
        if check(1, 2, 3) or check(1, 5, 9) or check(1, 4, 7):
            return True
    if board[0][1] != " ":
        if check(2, 5, 8):
            return True
    if board[0][2] != " ":
        if check(3, 5, 7) or check(3, 6, 9):
            return True
    if board[1][0] != " ":
        if check(4, 5, 6):
            return True
    if board[2][0] != " ":
        if check(7, 8, 9):
            return True

def ease_bot(bot):
    bot_rnd = random.randint(1, 9)
    bot_x, bot_y = convertCoord(bot_rnd)
    if board[bot_x][bot_y] == " ":
        board[bot_x][bot_y] = bot
    else:
        return False
    
def generate_step(player):
    if board[0][1] == player and board[0][2] == player or board[1][0] == player and board[2][0] == player or board[1][1] == player and board[2][2] == player:
        return 1
def medium_bot(bot,player):
    res = generate_step(player)
    if not res:
        res = random.randint(1, 9)
    bot_x, bot_y = convertCoord(res)
    if board[bot_x][bot_y] == " ":
        board[bot_x][bot_y] = bot
    else:
        return False
# False - error value
# True - win user
def player_run(player):
    choice = int(input(f"Enter number [{player}] :: "))
    if choice < 1 or choice > 9:
        return False
    user_x, user_y = convertCoord(choice)
    if board[user_x][user_y] == " ":
        board[user_x][user_y] = player
    if checkAll():
        print(f"Congratulation!!! Player {player}")
        return True


def start_game():
    user = "X"
    bot = "O"  # or player 2
    while True:
        counter = 0
        reset()
        game = int(input(''' 
                        1 - Player - Player
                        2 - Player - Bot
                        Enter :: '''))
        printBoard()
        if game == 2:
            level = int(input('''
                                        1 - Ease
                                        2 - Medium
                                        Enter :: '''))
        player = True if user == "X" else False
        while counter < 9:
            if game == 1:
                if player:
                    res = player_run(user)
                    if res == False:
                        continue
                    if res == True:
                        break
                    player = False
                    counter += 1
                else:
                    res = player_run(bot)
                    if res == False:
                        continue
                    if res == True:
                        break
                    player = True
                    counter += 1
            else:
                
                if player:
                    res = player_run(user)
                    if res == False:
                        continue
                    if res == True:
                        break
                    player = False
                    counter += 1
                else:
                    if level == 1:
                        res = ease_bot(bot)
                    elif level == 2:
                        res = medium_bot(bot, user)
                    if res == False:
                        continue
                    if checkAll():
                        print("Sorry!!! You Loser! Win O")
                        break
                    player = True
                    counter += 1

            printBoard()
        else:
            print("Draw")
        printBoard()
        exit_ = input("try again [yes/no]")
        if exit_ == "no":
            break
        user,bot = bot, user
        
start_game()
