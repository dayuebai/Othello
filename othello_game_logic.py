# Dayue Bai 35439000
# dayueb@uci.edu
#
# othello_game_logic.py
#
# ICS 32 Winter 2017
# Project #5: The Width of a Circle (Part 2)


# Use constants in place of hard-coded values

NONE = 0
BLACK = 1
WHITE = -1


# Eight extending possible directions list

DIRECTIONS = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]


class InvalidMoveError(Exception):
    """
    Raised whenever an invalid move is made
    """
    pass


class GameOverError(Exception):
    """
    Raised whenever an attempt is made to make a move after
    the game is already over
    """
    pass


class RoundOverError(Exception):
    """
    Raised whenever an attempt is made to make a mvoe after
    the current turn player has no valid move
    """
    pass


class GameState:
    """
    GameState object represents the current state of an Othello
    game, with methods that manipulate the state and get properties
    of the game state
    """
    def __init__(self, initial_state: [[int]], first_turn: int):
        """
        Initializes the GameState to have the given initial state
        and the first turn
        """
        self.state = initial_state
        self.turn = first_turn


    def _board_row_number(self) -> int:
        """
        Returns the number of rows on the board
        """
        row_number = len(self.state)
        return row_number


    def _board_column_number(self) -> int:
        """
        Returns the number of columns on the board
        """
        column_number = self.state[0]
        return len(column_number)

    
    def move(self, row_number: int, column_number: int) -> None:
        """
        Given a row number and a column number, update the game state
        that results when the current turn player drop a pience on the
        board. If input numbers are invalid, a ValueError is raised. If
        the game is over, a GameOverError is raised. If the current turn
        player cannot make a valid move, a RoundOverError is raised. If a
        move cannot be made on the board, an InvalidMoveError is raised
        """
        _require_valid_number(row_number, self._board_row_number())
        _require_valid_number(column_number, self._board_column_number())
        self.check_game_over()
        self.check_round_over()
        
        adjacent_directions = self._get_adjacent_directions(row_number, column_number, DIRECTIONS)
        validity, flip_pieces_ranges = self._check_valid_move(row_number, column_number, adjacent_directions)
        
        if self._check_cell(row_number, column_number, NONE) and validity:

            for flip_range in flip_pieces_ranges:
                
                rowdelta, coldelta, delta_border = flip_range

                for coefficient in range(delta_border + 1):
                    # make a move and flip pieces in the range
                    self.state[row_number + coefficient * rowdelta][column_number + coefficient * coldelta] = self.turn

            self.turn = _opposite_turn(self.turn) # set the turn to opposite turn
                                                  # for next round player
        else:
            raise InvalidMoveError()
    
                    
    def game_winner(self, winning_way: str) -> int:
        """
        Returns the player number with the most discs on the board in
        the final game state if the winning way is '>'; returns the fewest
        if the winning way is '<'. Anyway, if the final score is tied, return
        constant NONE
        """
        if winning_way == '>':
            if self.disc_number(BLACK) > self.disc_number(WHITE):
                return BLACK
            elif self.disc_number(BLACK) < self.disc_number(WHITE):
                return WHITE
            else:
                return NONE
            
        elif winning_way == '<':
            # multiply the winner number under
            # winning way: '>' by -1 will get
            # the winner number under winning
            # '<', because constant BLACK is the
            # opposite number of constant WHITE
            # and constant NONE * -1 = NONE
            return self.game_winner('>') * (-1)


    def disc_number(self, disc_color: int) -> int:
        """
        Returns the number of discs with the given color in the board
        """
        disc_number = 0
        
        for row in self.state:
            for disc in row:
                if disc == disc_color:
                    disc_number += 1

        return disc_number

    
    def check_game_over(self) -> None:
        """
        Raises a GameOverError if the given game state represents a situation
        where the game is over (i.e., there is a winning player); nothing happens
        otherwise
        """
        round_turn = self.turn
        game_over_signal = True
        check_attempt = 0

        # check two times to see if any one player
        # can make a valid move
        while game_over_signal and check_attempt < 2: 
            
            check_attempt += 1
            self.turn = _opposite_turn(self.turn)

            game_over_signal = self._check_over_result()

        # after checking, set the player's
        # turn to the current player
        self.turn = round_turn 
        
        if game_over_signal:
            raise GameOverError()


    def check_round_over(self) -> None:
        """
        Raises a RoundOverError and reverts back to the opposite turn
        if the given game state represents a situation where the current
        player cannot make a valid move
        """
        round_over_signal = True
        
        round_over_signal = self._check_over_result()

        if round_over_signal:
            self.turn = _opposite_turn(self.turn)
            raise RoundOverError()


    def _check_over_result(self) -> bool:
        """
        Returns False if any piece on the gameboard can make a valid move;
        returns True otherwise
        """
        over_signal = True
        
        for row_index in range(len(self.state)):
            for col_index in range(len(self.state[row_index])):
            
                adjacent_directions = self._get_adjacent_directions(row_index, col_index, DIRECTIONS)
                validity = self._check_valid_move(row_index, col_index, adjacent_directions)[0]

                if validity and self.state[row_index][col_index] == NONE:
                    over_signal = False

        return over_signal

    
    def _get_adjacent_directions(self, row_number: int, column_number: int, direction_list:[tuple]) -> [tuple]:
        """
        Returns a list of tuples with each tuple representing a valid direction, in
        which the given piece has an adjacent piece with opposite color
        """
        adjacent_directions = []
        opposite_turn = _opposite_turn(self.turn)
        
        for direction in direction_list:
            
            rowdelta, coldelta = direction
            
            if _is_valid_number(row_number + rowdelta, self._board_row_number()) and \
               _is_valid_number(column_number + coldelta, self._board_column_number()):

                if self._check_cell(row_number + rowdelta, column_number + coldelta, opposite_turn):
                    adjacent_directions.append(direction)

        return adjacent_directions


    def _check_valid_move(self, row_number: int, column_number: int, direction_list: [tuple]) -> None:
        """
        Returns True and a list of pieces needed to be flipped if the given move is a
        move; returns False and None otherwise
        """
        flip_pieces_ranges = []
        
        for direction in direction_list:
            delta_border = 2
            rowdelta, coldelta = direction

            while True:
                    row_line = row_number + rowdelta * delta_border
                    column_line = column_number + coldelta * delta_border

                    if _is_valid_number(row_line, self._board_row_number()) and \
                       _is_valid_number(column_line, self._board_column_number()):

                        # there is a sandwich pattern of pieces
                        if self._check_cell(row_line, column_line, self.turn):
                            flip_pieces_ranges.append((rowdelta, coldelta, delta_border))
                            break

                        # there cannot be a sandwich pattern of pieces
                        # in this direction
                        elif self._check_cell(row_line, column_line, NONE):
                            break
                        
                        # the piece is still in opposite turn's color,
                        # move one more unit in this direction
                        else:
                            delta_border += 1
                            
                    else:
                        break
                    
        if len(flip_pieces_ranges) != 0:
            return True, flip_pieces_ranges
        else:
            return False, None


    def _check_cell(self, row_number: int, column_number: int, color: int) -> bool:
        """
        Returns True if the color of the disc in the given cell is the same
        as the given color; returns False otherwise
        """
        return self.state[row_number][column_number] == color


# Private useful functions in implementing the game rule of othello
def _require_valid_number(input_number: int, standard_number: int) -> None:
    """
    Raises a value error if its parameter is not a valid input number
    """
    if type(input_number) != int or not _is_valid_number(input_number, standard_number):
        raise ValueError


def _is_valid_number(input_number: int, standard_number: int) -> bool:
    """
    Returns True if the given column number is valid; returns False otherwise
    """
    return 0 <= input_number < standard_number


def _opposite_turn(turn: int) -> int:
    """
    Given the player whose turn it is now, returns the opposite player
    """
    if turn == BLACK:
        return WHITE
    else:
        return BLACK

















    
