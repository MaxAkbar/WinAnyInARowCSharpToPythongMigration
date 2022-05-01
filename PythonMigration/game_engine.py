from game_result import game_result

class any_in_a_row_game_engine:
    win_in_a_Row = 0
    game_board = []
    game_status = -1

    def validate_win_in_a_row(self, in_a_row_win):
        if self.win_in_a_Row -1 == in_a_row_win:
            return True
        return False

    def get_next_player(self, player):
        if player == 1:
            return 2
        return 1

    def validate_board_cells(self, current_row, current_col, compare_row, compare_col, next_in_a_row):
        current_cell = self.game_board[current_row][current_col]
        compare_cell = self.game_board[compare_row][compare_col]

        if current_cell == compare_cell and not current_cell == 0:
            next_in_a_row += 1
            return True, next_in_a_row
        return False, 0

    def validate_in_a_row(self, game_board_rows, game_board_columns, win_in_a_row):
        min_board_size = min(game_board_rows, game_board_columns)

        if min_board_size < win_in_a_row:
            raise ValueError(f"Win in a row value {min_board_size} is greater than board size!")
        
        if min_board_size < 3:
            raise ValueError(f"Board size {min_board_size} must be greater than 3!")

        if win_in_a_row < 3:
            raise ValueError(f"Win in a row {min_board_size} must be greater than 3!")

    def init_game_board(self, game_board_rows, game_board_columns):
        self.game_board = [[0] * game_board_columns for _ in range(game_board_rows)]

    def __init__(self, game_board_rows, game_board_columns, win_in_a_row):
        self.validate_in_a_row(game_board_rows, game_board_columns, win_in_a_row)
        self.init_game_board(game_board_rows, game_board_columns)
        self.win_in_a_Row = win_in_a_row

    def make_a_move(self, current_player, user_input_row, user_imput_column):
        _game_result = game_result()
        _game_result.valid_move = False

        if user_input_row < len(self.game_board) and user_imput_column < len(self.game_board[0]):
            current_marker = self.game_board[user_input_row][user_imput_column]

            if current_marker == 1 or current_marker == 2:
                _game_result.message = "Placement has already a marker please select another placement."
            else:
                self.game_board[user_input_row][user_imput_column] = current_player
                _game_result.valid_move = True
        else:
            _game_result.message = "Invalid value please select another placement."
        return _game_result

    def check_winner(self, user_input_row, user_imput_column):
        if self.is_game_winner(user_input_row, user_imput_column):
            return 1

        if self.is_game_draw():
            return 2
        return 0

    def is_game_draw(self):
        for row in range(0, len(self.game_board)):
            for col in range(0, len(self.game_board[0])):
                if (self.game_board[row][col] == 0):
                    return False
        return True

    def is_game_winner(self, row, col):
        if (self.is_horizontal_cells_same(row, col)):
            return True

        if (self.is_vertical_cells_same(row, col)):
            return True

        if (self.is_diagonal_left_to_right_cells_same(row, col)):
            return True

        if (self.is_diagonal_right_to_left_cells_same(row, col)):
            return True
        return False
 
    def is_diagonal_right_to_left_cells_same(self, row, col):
        int_a_row_win = 0
        row_position = row + 1
        col_position = col - 1

        while row_position < len(self.game_board) and col_position > 0:
            success, int_a_row_win = self.validate_board_cells(row, col, row_position, col_position, int_a_row_win)
            if success:
                row_position += 1
                col_position -= 1

                continue
            break

        if int_a_row_win < self.win_in_a_Row - 1:
            row_position = row - 1
            col_position = col + 1
            
            while row_position >= 0 and col_position < len(self.game_board[0]):
                success, int_a_row_win = self.validate_board_cells(row, col, row_position, col_position, int_a_row_win)
                if success:
                    row_position -= 1
                    col_position += 1

                    continue
                break
                
        return self.validate_win_in_a_row(int_a_row_win)

    def is_diagonal_left_to_right_cells_same(self, row, col):
        int_a_row_win = 0
        row_position = row + 1
        col_position = col + 1

        while row_position < len(self.game_board) and col_position < 0:
            success, int_a_row_win = self.validate_board_cells(row, col, row_position, col_position, int_a_row_win)
            if success:
                row_position += 1
                col_position += 1

                continue
            break

        if int_a_row_win < self.win_in_a_Row - 1:
            row_position = row - 1
            col_position = col - 1
            
            while row_position >= 0 and col_position >= 0:
                success, int_a_row_win = self.validate_board_cells(row, col, row_position, col_position, int_a_row_win)
                if success:
                    row_position -= 1
                    col_position -= 1

                    continue
                break
                
        return self.validate_win_in_a_row(int_a_row_win)

    def is_vertical_cells_same(self, row, col):
        int_a_row_win = 0
        row_position = row + 1

        while row_position < len(self.game_board):
            success, int_a_row_win = self.validate_board_cells(row, col, row_position, col, int_a_row_win)
            if success:
                row_position += 1

                continue
            break

        if int_a_row_win < self.win_in_a_Row - 1:
            row_position = row - 1
            while row_position >= 0:
                success, int_a_row_win = self.validate_board_cells(row, col, row_position, col, int_a_row_win)
                if success:
                    row_position -= 1

                    continue
                break

        return self.validate_win_in_a_row(int_a_row_win)

    def is_horizontal_cells_same(self, row, col):
        int_a_row_win = 0
        col_position = col + 1

        while col_position < len(self.game_board):
            success, int_a_row_win = self.validate_board_cells(row, col, row, col_position, int_a_row_win)
            if success:
                col_position += 1
                
                continue
            break

        if int_a_row_win < self.win_in_a_Row - 1:
            col_position = col - 1
            while col_position >= 0:
                success, int_a_row_win = self.validate_board_cells(row, col, row, col_position, int_a_row_win)
                if success:
                    col_position -= 1
                
                    continue
                break

        return self.validate_win_in_a_row(int_a_row_win)
