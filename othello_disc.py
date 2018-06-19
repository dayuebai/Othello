# Dayue Bai 35439000
# dayueb@uci.edu
#
# othello_disc.py
#
# ICS 32 Winter 2017
# Project #5: The Width of a Circle (Part 2)


class Disc:
    """
    The class Disc represents each disc on the othello game board.
    The attributes built in the class indicate the disc's position
    on the game board, and the disc's color
    """
    def __init__(self, row_index: int, column_index: int, color: int) -> None:
        """
        Initializes a Spot object, given its zero based row number, column number
        and color
        """
        self.row_index = row_index
        self.column_index = column_index
        self.color = color


# Public function
def from_pixel(pixel_y: float, pixel_x: float, row_delta: float, column_delta: float, color: int) -> Disc:
    """
    Builda a Spot object given its pixel x and y coordinates, along with the width and height
    of each cell on the othello game board (necessary for coversion to the Spot's position(
    zero based row number and column number on the board)
    """
    return Disc(int(pixel_y // row_delta), int(pixel_x // column_delta), color)


    

    
