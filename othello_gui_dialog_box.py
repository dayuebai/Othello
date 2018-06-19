# Dayue Bai 35439000
# dayueb@uci.edu
#
# othello_gui_dialog_box.py
#
# ICS 32 Winter 2017
# Project #5: The Width of a Circle (Part 2)


import tkinter


# Specify a default font as a global constant and
# use the defautld font in implementing the dialog box

_DEFAULT_FONT = ('Helvatica', 14)


class QuestionDialog:
    """
    The QuestionDialog class creates represent a modal dialog box and asks
    the user how many rows and columns are on the board, who moves first and
    how the game will be won. After the user fill out all the information and
    presses either OK or CANCEL, we can ask the object which button was used
    to dismiss the dialog and what values were in the widgets in which the
    user could fill out the information about the game board.
    """
    def __init__(self) -> None:
        # A Toplevel object is, to the 'root window' of the dialog box, as
        # the Tk object to the entire application. It's not the root window
        # of an entire application; it's a seperate, additional window.
        self._dialog_window = tkinter.Toplevel()

        # Sets the title of the dialog box
        self._dialog_window.title('Game Board Setting')

        # Set the position of the modal dialog box,
        # at which it pops up in the desktop.
        self._dialog_window.geometry('450x350+490-100')

        # Creates and lays out some widgets inside the Toplevel obejct.
        #
        # BANNER
        self._banner_text = tkinter.StringVar()
        self._banner_text.set('Customize Your Othello Game Board...')
        
        banner_label = tkinter.Label(
            master = self._dialog_window,
            textvariable = self._banner_text,
            font = ('Helvatica', 20))

        banner_label.grid(
            row = 0, column = 0, columnspan = 2,
            padx = 10, pady = 10, sticky = tkinter.W)
        
        # ROW NUMBER SETTING
        row_number_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Row number on the board:',
            font = _DEFAULT_FONT)

        row_number_label.grid(row = 1, column = 0,
                              padx = 10, pady = 10, sticky = tkinter.W)
        
        master = self._dialog_window
        self._row_var = tkinter.IntVar()
        self._row_var.set('Select row number')
        
        # The row number and the column number
        # must both be even integers between 4
        # and 16 inclusive.
        options = tuple(range(4,18,2))
        
        self._row_number_menu = tkinter.OptionMenu(master, self._row_var, *options)

        self._row_number_menu.grid(
            row = 1, column = 1, padx = 10, pady = 1,
            sticky = tkinter. E + tkinter.W)
        
        # COLUMN NUMBER SETTING
        column_number_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Column number on the board:',
            font = _DEFAULT_FONT)

        column_number_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        
        self._column_var = tkinter.IntVar()
        self._column_var.set('Select column number')
        
        self._column_number_menu = tkinter.OptionMenu(master, self._column_var, *options)

        self._column_number_menu.grid(
            row = 2, column = 1, padx = 10, pady = 1,
            sticky = tkinter.E + tkinter.W)
        
        # FIRST TURN SETTING
        first_turn_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Who moves first:',
            font = _DEFAULT_FONT)

        first_turn_label.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        
        self._turn_var = tkinter.IntVar()
        
        self._first_turn_radiobutton1 = tkinter.Radiobutton(
            master = self._dialog_window,
            text = 'BLACK',
            variable = self._turn_var,
            value = 1)

        self._first_turn_radiobutton1.grid(
            row = 3, column = 1, padx = 10, pady =1,
            sticky = tkinter.W)
        
        self._first_turn_radiobutton2 = tkinter.Radiobutton(
            master = self._dialog_window,
            text = 'WHITE',
            variable = self._turn_var,
            value = -1)

        self._first_turn_radiobutton2.grid(
            row = 4, column = 1, padx = 10, pady =1,
            sticky = tkinter.W)

        # WINNING WAY SETTING
        winning_way_label = tkinter.Label(
            master = self._dialog_window,
            text = 'How players win:',
            font = _DEFAULT_FONT)

        winning_way_label.grid(
            row = 5, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        
        self._win_var = tkinter.IntVar()
        
        self._winning_way_radiobutton1 = tkinter.Radiobutton(
            master = self._dialog_window,
            text = '>: Player with more discs wins',
            variable = self._win_var,
            value = 1)

        self._winning_way_radiobutton1.grid(
            row = 5, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W)

        self._winning_way_radiobutton2 = tkinter.Radiobutton(
            master = self._dialog_window,
            text = '<: Player with less discs wins',
            variable = self._win_var,
            value = -1)

        self._winning_way_radiobutton2.grid(
            row = 6, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W)

        # BUTTON FRAME
        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(
            row = 7, column = 0, columnspan = 2,
            padx = 10, pady = 10, sticky = tkinter.S + tkinter.E)

        # OK BUTTON
        ok_button = tkinter.Button(
            master = button_frame,
            text = 'OK',
            font = _DEFAULT_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        # CANCEL BUTTON
        cancel_button = tkinter.Button(
            master = button_frame,
            text = 'CANCEL',
            font = _DEFAULT_FONT,
            command = self._on_cancel_button)

        cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)

        self._dialog_window.rowconfigure(0, weight = 1)
        self._dialog_window.rowconfigure(1, weight = 1)
        self._dialog_window.rowconfigure(2, weight = 1)
        self._dialog_window.rowconfigure(3, weight = 1)
        self._dialog_window.rowconfigure(4, weight = 1)
        self._dialog_window.rowconfigure(5, weight = 1)
        self._dialog_window.rowconfigure(6, weight = 1)
        self._dialog_window.rowconfigure(7, weight = 1)

        self._dialog_window.columnconfigure(1, weight = 1)

        # ATTRIBUTES
        #
        # Initialize some attributes that will carry information
        # about the outcome of this dialog box.
        self.ok_clicked = False
        self.row_number = None
        self.column_number = None
        self.first_turn = None
        self.winning_way = None


    def pop(self) -> None:
        """
        Turns control over to dialog box and make dialog box modal
        """
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()


    # The following five methods allows us to ask dialog box, after it's
    # dismissed, what happened. We can know what information was in the four
    # input widgets and whether OK or CANCEL is clicked by the user.
    
    def was_ok_clicked(self) -> bool:
        """
        Returns True if OK button is clicked and all the information
        are filled out by the user
        """
        return self.ok_clicked


    def get_row_number(self) -> int:
        """
        Returns the row number on the board assigned by the user
        """
        return self.row_number


    def get_column_number(self) -> int:
        """
        Returns the column number on th board assigned by the user
        """
        return self.column_number


    def get_first_turn(self) -> int:
        """
        Returns the symbol number of the player who move first
        """
        return self.first_turn


    def get_winning_way(self) -> int:
        """
        Returns the symbol number representing how the game will be won.
        If it returns 1, the user assigns the player with more discs to be
        the winner. If it returns -1, the users assigns the player with less
        discs to be the winner
        """
        return self.winning_way


    # The following two method are command handlers of
    # the OK and CANCEL button, repsectively.
    def _on_ok_button(self) -> None:
        """
        If the user fill out all the information in the dialog box, self._ok_clicked
        will be set to True and the dialog box window will be dismissed. Meanwhile,
        all the user input information will be extracted from the widgets and assigned
        to corresponding attributes.
        """
        try:                               
            self.row_number = self._row_var.get()
            self.column_number = self._column_var.get()
            self.first_turn = self._turn_var.get()
            self.winning_way = self._win_var.get()

            # if the user does not fill out the information about
            # first move player and how games will be won. The default
            # value of self._first turn and self._winning way will be set
            # to 0, automatically.If the values of the two variables are
            # both not 0. self._ok_clicked and the dialog window will be dismissed.
            if self.first_turn != 0 and self.winning_way != 0:
                self.ok_clicked = True
                self._dialog_window.destroy()

        # TclError will be raised if the above self._row_var.get()
        # and self._column_var.get()methods get unexpected type of value,
        # because the user does not fill out the information about how many 
        # rows or columns are on the board. We assign a string type of value
        # to the IntVar(), so if the user does not fill out the information
        # TclError will be raised and the banner text will be set to give
        # the user a tip that they need to fill out all information.
        except tkinter.TclError:
            self._banner_text.set('Please fill out all information')

        # If the user does not fill out the information about who moves
        # first and how the game will be won, the banner text will be set
        # to 'Please fill out all information'.
        else:
            self._banner_text.set('Please fill out all information')


    def _on_cancel_button(self) -> None:
        """
        Called after the users clicks the CANCEL button,
        so that the dialog box window will be dismissed
        and pop() method will return. The control will be
        turned over to Tk object
        """
        self._dialog_window.destroy()
