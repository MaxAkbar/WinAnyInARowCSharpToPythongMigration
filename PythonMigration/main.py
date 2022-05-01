import os

from game_engine import any_in_a_row_game_engine


#board = [
#            [ 0, 0, 0, 0, 0, 0, 0, 1 ],
#            [ 0, 0, 0, 0, 0, 0, 1, 0 ],
#            [ 0, 0, 0, 0, 0, 1, 0, 0 ],
#            [ 0, 0, 0, 0, 1, 0, 0, 0 ],
#            [ 0, 0, 0, 1, 0, 0, 0, 0 ],
#            [ 0, 0, 0, 0, 0, 0, 0, 0 ],
#            [ 0, 0, 0, 0, 0, 0, 0, 0 ],
#            [ 0, 0, 0, 0, 0, 0, 0, 0 ],
#        ]

#board = [
#            [ 1, 2, 2],
#            [ 1, 0, 0],
#            [ 1, 0, 0],
#        ]

#game_engine = any_in_a_row_game_engine(len(board), len(board[0]), 3)
#game_engine.game_board = board
#test = game_engine.check_winner(2, 0)


# default values
board_game_size = 8
win_in_a_row = 5
current_player = -1
game_status = 0
keep_looping = True

def heads_up_display(player_number):
    print("Welcome to the Super Duper Tic Tac Toe Game!")
    print("Player 1: X")
    print("Player 2: O")
    print()
    print(f"Player {player_number} to move, select 1 through 9 from the game board.")
    print()

def get_player_marker(player):
    if player % 2 == 0:
        return 'O'

    return 'X'

def print_console(loop_counter, print_digit, print_digits, increment_print_digits):
    print(print_digit, end ="");

    for i in range(0, loop_counter):
        if i + increment_print_digits > 8:
            print_digits = print_digits.replace("   ", "  ");
    
        print(print_digits.format(i + increment_print_digits), end ="")

    print();

def draw_gameboard(board):
    print_console(len(board[0]), "     ", "{0}   ", 1);
    print_console(len(board[0]), "   -", str("-"*4), 0);

    for row in range(len(board)):
        space = "  ";

        if row > 8:
            space = " ";
    
        print(f"{row + 1}{space}", end = "")
                
        for col in range(len(board[0])):
            current_column = board[row][col]
            current_column_ui = ' '
                    
            if current_column != 0:
                current_column_ui = get_player_marker(current_column)
        
            print(f"| {current_column_ui} ", end = "")
        

        print("|")

        print_console(len(board[0]), "   -", str('-'*4), 0)

while keep_looping:
    os.system("cls")

    print("Welcome to our Super Duper Win in any Row game.");
    print("Please select the game board size by selecting a numeric value: ", end="")
    board_game_size = input()
    
    if board_game_size.isnumeric() == False:
        print()
        print("Please select a numeric value!")
        print("Select any key to start over.")
        input()

        continue

    print(f"Please select the game win in a row must be smaller than {board_game_size} : ", end="")

    win_in_a_row = input()
    
    if win_in_a_row.isnumeric() == False:
        print()
        print("Please select a numeric value!")
        print("Select any key to start over.")
        input()

        continue
    
    keep_looping = False

main_game_loop = True
game_engine = any_in_a_row_game_engine(int(board_game_size), int(board_game_size), int(win_in_a_row))

while main_game_loop:
    os.system("cls")

    current_player = game_engine.get_next_player(current_player)
    inner_game_loop = False

    heads_up_display(current_player)
    draw_gameboard(game_engine.game_board)
    
    while not inner_game_loop:

        print("Please select a numeric value for the row: ", end = '')

        user_input_row = int(input()) -1

        print("Please select a numeric value for the column: ", end = '')

        user_input_col = int(input()) -1

        game_result = game_engine.make_a_move(current_player, user_input_row, user_input_col)

        if not game_result.valid_move:
            print(game_result.message)

        game_engine.game_status = game_engine.check_winner(user_input_row, user_input_col)

        inner_game_loop = game_result.valid_move

    if game_engine.game_status == 0:
        main_game_loop = True

os.system("cls")

heads_up_display(current_player)
draw_gameboard(game_engine.game_board)

if game_engine.game_status == 1:
    print(f"Player {current_player} is the winner!")

if game_engine.game_status == 2:
    print(f"The game is a draw!")
