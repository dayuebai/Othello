# Dayue Bai 35439000
# dayueb@uci.edu
#
# othello_initial_board.py
#
# ICS 32 Winter 2017
# Project #5: The Width of a Circle (Part 2)


# Import othello_disc to create Disc class
# Each Disc object is itself represented as a
# disc that can be manipulated and drawn
# on the game board

import othello_disc


class InitialBoard:
    # The InitialBoard class represents the initial state of the othello game
    # board, that can be manipulated by setting a disc on the board, when the
    # set the initial game board
    def __init__(self, row_number: int, column_number: int) -> None:
        """
        Initializes the initial state of the othello gameboard. Initially,
        there are no discs on the game board. Use 0 to symbolize the cell
        has no disc inside and 1 and -1 to stand for the BLACK and WHITE
        disc in the cell. 
        """
        self.state = []

        for row_index in range(row_number):
            
            self.state.append([])
            
            for column_index in range(column_number):
                self.state[row_index].append(0)

        
    def set_disc(self, disc: othello_disc.Disc) -> None:
        """
        Set a disc on the othello game board, given the user-set disc,
        during initial game board setting, if the cell has no disc.
        """
        try:
            # Checks if the clicked cell already has a disc inside
            if self.state[disc.row_index][disc.column_index] == 0:
                self.state[disc.row_index][disc.column_index] = disc.color

        # If the user clicks the right or bottom border line of the othello
        # game board, an IndexError will be raised (since the row and column
        # number of the game state are both zero based), so skip such user
        # invalid click
        except IndexError:
            pass
