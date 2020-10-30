BOARD_STATUS = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
POSITIONS = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

MATCH_WINNER = "0"
FIRST_PLAYER = "1"
SECOND_PLAYER = "2"
FIRST_PLAYER_MARK = "X"
SECOND_PLAYER_MARK = "O"
FIRST_PLAYER_SCORE = 0
SECOND_PLAYER_SCORE = 0

YES = "Y"
NO = "N"
ONE = "1"
TWO = "2"
CROSS = "X"
CIRCLE = "O"

INSTRUCTIONS1 = "On your turn, use the numeric keyboard to choose"
INSTRUCTIONS2 = "a position on the board as follows"

FIRST_MATCH = "Play? (Y/N): "
SET_FIRST_PLAYER = "Who will be the First Player? (1/2): "
SET_PLAYERS_MARKS = "What will be the First Player mark? (X/O): "
COMMITED_PLAYERS_MARKS = "Marks"
CONTINUE = "Another match? (Y/N): "
FINAL_SCORE = "Final Score"
MATCH_END = "Game End! Winner is "

#-------------------------------------------------------------

#COMPLETE
def wrong_input(type1, type2):
    return "Wrong Input, please type '{0}' or '{1}': ".format(type1, type2)

def wrong_play():
    return "Wrong Play, please type a valid position: "


#COMPLETE
def game_loop():
    nm = print_instructions()
    if nm:
        set_game()
    while nm:
        nm = play_match()
    display_final_score()
    return True


#COMPLETE
def print_instructions():
    nm = "nextmatch"
    print("\n\n")
    print(INSTRUCTIONS1)
    print(INSTRUCTIONS2)
    print_board()
    nm = str(input(FIRST_MATCH))
    while True:
        if nm.lower() == "y":
            return True
        elif nm.lower() == "n":
            return False
        nm = str(input(wrong_input(YES,NO)))


#COMPLETE
def set_game():
    fp = 0
    fpmark = CROSS
    global FIRST_PLAYER
    global SECOND_PLAYER
    global FIRST_PLAYER_MARK
    global SECOND_PLAYER_MARK
    fp = str(input(SET_FIRST_PLAYER))
    while True:
        if fp.lower() == ONE:
            FIRST_PLAYER = ONE
            SECOND_PLAYER = TWO
            break
        elif fp.lower() == TWO:
            FIRST_PLAYER = TWO
            SECOND_PLAYER = ONE
            break
        fp = str(input(wrong_input(ONE,TWO)))

    fpmark = str(input(SET_PLAYERS_MARKS))
    while True:
        if fpmark.lower() == "x":
            FIRST_PLAYER_MARK = CROSS
            SECOND_PLAYER_MARK = CIRCLE
            break
        if fpmark.lower() == "o":
            FIRST_PLAYER_MARK = CIRCLE
            SECOND_PLAYER_MARK = CROSS
            break
        fpmark = str(input(wrong_input(CROSS,CIRCLE)))
    COMMITED_PLAYERS_MARKS = "First Player will be {0} and Second Player will be {1}".format(
            FIRST_PLAYER_MARK, SECOND_PLAYER_MARK)
    print(COMMITED_PLAYERS_MARKS)
    clean_board()

#COMPLETE
def clean_board():
    for num in range(0,9):
        BOARD_STATUS[num] = " "

#COMPLETE
def play_match():
    nm = "nextmatch"
    game = True
    next_player = FIRST_PLAYER
    while game:
        print_board()
        next_player = get_play(next_player)
        game = check_win_condition()

    print_board()
    clean_board()
    print_match_winner()
    nm = str(input(CONTINUE))
    while True:
        if nm.lower() == "y":
            return True
        if nm.lower() == "n":
            return False
        nm = str(input(wrong_input(YES,NO)))


#COMPLETE
def print_board():
    print("\n")
    print("  {0}|{1}|{2}".format(BOARD_STATUS[6],BOARD_STATUS[7],BOARD_STATUS[8]))
    print("  -----")
    print("  {0}|{1}|{2}".format(BOARD_STATUS[3],BOARD_STATUS[4],BOARD_STATUS[5]))
    print("  -----")
    print("  {0}|{1}|{2}".format(BOARD_STATUS[0],BOARD_STATUS[1],BOARD_STATUS[2]))
    print("\n")


#COMPLETE
def get_play(next_player):
    check = False
    playspace = str(input("Player {0} Turn: ".format(next_player)))
    while True:
        if playspace in POSITIONS:
            space = BOARD_STATUS[int(playspace)-1]
            if space not in [CROSS,CIRCLE]:
                if next_player == FIRST_PLAYER:
                    BOARD_STATUS[int(playspace)-1] = FIRST_PLAYER_MARK
                    check = True
                else:
                    BOARD_STATUS[int(playspace)-1] = SECOND_PLAYER_MARK
                    check = True
                if check:
                    if next_player == ONE:
                        return TWO
                    else:
                        return ONE
        playspace = str(input(wrong_play()))


#COMPLETE
def check_win_condition():
    global MATCH_WINNER
    if check_player_win(FIRST_PLAYER_MARK):
        global FIRST_PLAYER_SCORE
        FIRST_PLAYER_SCORE += 1
        MATCH_WINNER = "Player " + FIRST_PLAYER
        return False
    if check_player_win(SECOND_PLAYER_MARK):
        global SECOND_PLAYER_SCORE
        SECOND_PLAYER_SCORE += 1
        MATCH_WINNER = "Player " + SECOND_PLAYER
        return False
    if check_tie() == 0:
        MATCH_WINNER = "None"
        return False
    return True

#COMPLETE
def check_tie():
    spacecount = 0
    for num in BOARD_STATUS:
        if num not in [CROSS, CIRCLE]:
            spacecount += 1
    return spacecount

#COMPLETE
def check_player_win(mark):
    wincheck = 0
    wincheck += check_row_win(0,mark)
    wincheck += check_row_win(3,mark)
    wincheck += check_row_win(6,mark)
    wincheck += check_column_win(0,mark)
    wincheck += check_column_win(1,mark)
    wincheck += check_column_win(2,mark)
    wincheck += check_descending_diag_win(mark)
    wincheck += check_ascending_diag_win(mark)
    if wincheck >= 1:
        return True
    return False

#COMPLETE
def check_descending_diag_win(mark):
    if check_mark_position(6,mark):
        if check_mark_position(4,mark):
            if check_mark_position(2,mark):
                return 1
    return 0

#COMPLETE
def check_ascending_diag_win(mark):
    if check_mark_position(0,mark):
        if check_mark_position(4,mark):
            if check_mark_position(8,mark):
                return 1
    return 0

#COMPLETE
def check_column_win(col_starter,mark):
    if check_mark_position(col_starter,mark):
        if check_mark_position(col_starter+3,mark):
            if check_mark_position(col_starter+6,mark):
                return 1
    return 0

#COMPLETE
def check_row_win(row_starter,mark):
    if check_mark_position(row_starter,mark):
        if check_mark_position(row_starter+1,mark):
            if check_mark_position(row_starter+2,mark):
                return 1
    return 0

#COMPLETE
def check_mark_position(position, mark):
    if BOARD_STATUS[position] == mark:
        return True
    return False

#COMPLETE
def print_match_winner():
    print("\n")
    print(MATCH_END + MATCH_WINNER)
    print("\n")

#COMPLETE
def display_final_score():
    FINAL_SCORE = "Final Score \n\nPlayer 1: {0}\nPlayer 2: {1}".format(
        FIRST_PLAYER_SCORE, SECOND_PLAYER_SCORE)
    print(FINAL_SCORE)

# ==============================================
if __name__ == "__main__":
    game_loop()
# ==============================================

