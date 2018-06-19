# Dayue Bai 35439000
# dayueb@uci.edu
#
# othello_gui_main_window.py
#
# ICS 32 Winter 2017
#
# Project #5: The Width of a Circle (Part 2)


import tkinter


# Imports the following files to help
# build OthelloApplication class
import othello_disc
import othello_gui_dialog_box
import othello_initial_board
import othello_game_logic


# Default font used as a global constant
# in implementing othello gui
_DEFAULT_FONT = ('Helvetica', 20)


class OthelloApplication:
    """
    Creates a class to implement the graphical user
    interface of the Othello game application
    """
    def __init__(self) -> None:
        """
        Creates a Tk object to handle the main window, meanwhile, set the position
        at which the main window pops up in the desktop and the title of the main
        window. Then show the main menu frame (content) in the main window
        """
        self._root_window = tkinter.Tk()

        # Shows the content of the main menu
        # in the main window
        self._show_main_menu_frame()

        
    def _show_main_menu_frame(self) -> None:
        """
        Creates and lays out several widgets inside the Tk object
        """
        # Set title and position of the main window
        self._root_window.title('Othello Main Menu')
        self._root_window.geometry('900x700+275-100')
        
        # MAIN MENU FRAME
        self._main_menu_frame = tkinter.Frame(
            master = self._root_window, bg = '#996633')

        self._main_menu_frame.grid(
            row = 0, column = 0, rowspan = 4,
            sticky = tkinter.E + tkinter.W + tkinter.S + tkinter.N)

        # WELCOME LABEL
        game_welcome_label = tkinter.Label(
            master = self._main_menu_frame, text = 'Welcome To Play FULL Version Othello!',
            font = ('Helvetica', 30), bg = '#996633')
        
        game_welcome_label.grid(row = 0, column = 0, padx = 10, pady = 10)

        # START BUTTON
        self._start_button = tkinter.Button(
            master = self._main_menu_frame, text = 'START',
            font = _DEFAULT_FONT, command = self._on_start)

        self._start_button.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N)

        # QUIT BUTTON
        quit_button = tkinter.Button(
            master = self._main_menu_frame, text = 'QUIT',
            font = _DEFAULT_FONT, command = self._on_quit)

        quit_button.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N)

        # Resizes the grid cell and the main menu frame
        # as the size of the main window changes
        self._main_menu_frame.rowconfigure(0, weight = 1)
        self._main_menu_frame.rowconfigure(1, weight = 1)
        self._main_menu_frame.rowconfigure(2, weight = 1)
        self._main_menu_frame.columnconfigure(0, weight = 1)
        
        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.rowconfigure(2, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)


    def start(self) -> None:
        """
        Turns the control over to tkinter until the main window is dismissed
        """
        self._root_window.mainloop()


    def _on_start(self) -> None:
        """
        Pops up the Question dialog box, when the user clicks the OK button
        Turn conrol over to dialog box. It will not return until the user
        dismiss the dialog box
        """
        dialog = othello_gui_dialog_box.QuestionDialog()
        dialog.pop()
        
        winning_way_reference_dict = {1: '>', -1: '<'}

        if dialog.was_ok_clicked():
            self.row_number = dialog.get_row_number()
            self.column_number = dialog.get_column_number()
            self.first_turn = dialog.get_first_turn()
            self.winning_way = winning_way_reference_dict[dialog.get_winning_way()]

            # Hides main menu frame and shows
            # the game board frame
            self._main_menu_frame.grid_forget()
            self._set_game_board_frame()
        

    def _on_quit(self) -> None:
        """
        Destroys the main window and the start method will return,
        whenever the user clicks on the QUIT button
        """
        self._root_window.destroy()


    def _set_game_board_frame(self) -> None:
        """
        Sets the initial game board frame. Creates several widgets
        inside the game board frame
        """
        # Changes the title of the main window when the user
        # set the initial game board
        self._root_window.title('Othello Game Board Setting')

        # GAME BOARD FRAME
        self._game_board_frame = tkinter.Frame(
            master = self._root_window, bg = '#ffffb3')

        self._game_board_frame.grid(
            row = 0, column = 0, rowspan = 4, columnspan = 4,
            sticky = tkinter.E + tkinter.W + tkinter.S + tkinter.N)

        # INSTRUCTION TEXT
        self._instruction_text = tkinter.StringVar()
        self._instruction_text.set('Please click cell placing initial BLACK discs...')
        
        instruction_label = tkinter.Label(
            master = self._game_board_frame, textvariable = self._instruction_text,
            height = 2, font = ('Helvatica', 20), bg = '#ffffb3')

        instruction_label.grid(row = 0, column = 0, padx = 10, pady = 10)

        # BOARD CANVAS
        self._board_canvas = tkinter.Canvas(
            master = self._game_board_frame, width = 600, height = 600,
            background = '#996600', bd = 0)

        self._board_canvas.grid(row = 1, column = 0, padx = 5, pady = 5,
                                sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        # BUTTON FRAME
        self._option_frame = tkinter.Frame(
            master = self._game_board_frame, bg = '#ffffb3')

        self._option_frame.grid(row = 1, column = 1, rowspan = 1, sticky = tkinter.N)

        self._change_color_button = tkinter.Button(
            master = self._option_frame, text = 'Change Placed Disc Color',
            font = _DEFAULT_FONT, command = self._change_color)

        self._change_color_button.grid(
            row = 0, column = 0, padx = 10, pady = 100, 
            sticky = tkinter.W)

        self._start_game_button = tkinter.Button(
            master = self._option_frame, text = 'Start Othello Game', font = _DEFAULT_FONT,
            command = self._start_game)

        self._start_game_button.grid(
            row = 1, column = 0, padx = 10, pady = 50, 
            sticky = tkinter.W)

        self._board_canvas.bind('<Configure>', self._on_canvas_resized)
        self._board_canvas.bind('<Button-1>', self._on_canvas_set)

        self._game_board_frame.rowconfigure(1, weight = 1)
        self._game_board_frame.columnconfigure(0, weight = 1)
        
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

        # Set the first turn to BLACK DISC player,
        # when the user sets the initial game board
        self._set_turn = othello_game_logic.BLACK

        # Assigns the initial state of the game
        # board to a variable, by creating an
        # InitialBoard object
        self._current_state = othello_initial_board.InitialBoard(self.row_number, self.column_number)
        
        
    def _change_color(self) -> None:
        """
        Changes the color of the disc that will be
        set by the user on the game board, during
        initial game board setting
        """
        turn_text_reference_dict = {othello_game_logic.BLACK: 'Please click cell placing initial BLACK discs...',
                                    othello_game_logic.WHITE: 'Please click cell placing initial WHITE discs...'}
        
        # the number of BLAKC color is the
        # opposite number of the number of
        # WHITE disc
        self._set_turn = self._set_turn * (-1)

        # Change the instruction text, when the user
        # choose to set another color disc on the board
        # during the initial game board setting
        self._instruction_text.set(turn_text_reference_dict[self._set_turn])


    def _on_canvas_set(self, event: tkinter.Event) -> None:
        """
        Called whenever the canvas the is clicked during the initial game
        board setting. Handles the click by setting a disc on the user clicked
        cell 
        """
        width = self._board_canvas.winfo_width()
        height = self._board_canvas.winfo_height()

        row_delta = height / self.row_number
        column_delta = width / self.column_number

        # Create a disc object according the position
        # of the cell at which the user clicks on the board
        click_cell = othello_disc.from_pixel(
            event.y, event.x, row_delta, column_delta, self._set_turn)

        # Handles the click by setting a disc
        # on the board in initial game board setting
        self._current_state.set_disc(click_cell)

        # After handling the click, redraw the
        # game board and all of the discs
        self._redraw_game_board()


    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        """
        Whenver the Canvas's size changes, redraw all of the spots,
        since their size have changes, too.
        """
        self._redraw_game_board()


    def _start_game(self) -> None:
        """
        Creates and lays out several widgets in the gaem board frame.
        Handles the user's move.
        """
        # Changes the title of the main window when game starts
        self._root_window.title('Othello Game Board (FULL RULE)')

        # Hides the CHANGE PLACED DISC COLOR button
        # and the START OTHELLO GAME button
        self._change_color_button.grid_forget()
        self._start_game_button.grid_forget()
        
        self._board_canvas.bind('<Button-1>', self._on_canvas_move)

        # Assign the initial game state and the first turn number
        # to self._current_state, when othello game begins
        self._current_state = othello_game_logic.GameState(self._current_state.state, self.first_turn)

        self._color_reference_dict = {othello_game_logic.BLACK: 'BLACK',
                                      othello_game_logic.WHITE: 'WHITE'}

        self._winner_reference_dict = {othello_game_logic.BLACK: 'Congratulations!!! BLACK disc player wins',
                                       othello_game_logic.WHITE: 'Congratulations!!! WHITE disc player wins',
                                       othello_game_logic.NONE: 'Game Over! no one wins...'}

        # INSTRUCTION TEXT
        self._instruction_text.set('Turn: {}'.format(
            self._color_reference_dict[self._current_state.turn]))

        # BLACK SCORE LABEL
        # WHITE SCORE LABEL
        self._black_score_text = tkinter.StringVar()
        self._white_score_text = tkinter.StringVar()
        
        self._black_score_text.set('BLACK DISC:  {}'.format(self._current_state.disc_number(othello_game_logic.BLACK)))
        self._white_score_text.set('WHITE DISC:  {}'.format(self._current_state.disc_number(othello_game_logic.WHITE)))

        black_score_label = tkinter.Label(
            master = self._option_frame, textvariable = self._black_score_text,
            width = 16, justify = tkinter.LEFT, bg = '#ffffb3', font = _DEFAULT_FONT)

        black_score_label.grid(
            row = 0, column = 0, padx = 60, pady = 100,
            sticky = tkinter.W)

        white_score_label = tkinter.Label(
            master = self._option_frame, textvariable = self._white_score_text,
            width = 16, justify = tkinter.LEFT, bg = '#ffffb3', font = _DEFAULT_FONT)

        white_score_label.grid(
            row = 1, column = 0, padx = 60, pady = 50,
            sticky = tkinter.W)

        # Checks if the initial user-set game state
        # is a game over state or a round over state
        # (the current turn player cannot make a valid
        # move), when the game first starts
        try:
            self._current_state.check_game_over()
            self._current_state.check_round_over()

        # RoundOverError is raised. Switches the turn
        # and shows the corresponding turn information
        except othello_game_logic.RoundOverError:
            self._instruction_text.set('Turn: {}'.format(
                self._color_reference_dict[self._current_state.turn]))

        # GameOverError is rasied. Shows the game winner
        # information and the final option frame
        except othello_game_logic.GameOverError:
            winner_number = self._current_state.game_winner(self.winning_way)
            self._instruction_text.set(self._winner_reference_dict[winner_number])

            self._show_final_option_frame()


    def _on_canvas_move(self, event: tkinter.Event):
        """
        Handles the user's move (users's click on the board) Updates the
        game state of the game board. Checks the validity of the user's move.
        Checks if the game or the round is over after the user's move. Handles
        Raised Error by showing correspoding information and updating the game state
        """
        width = self._board_canvas.winfo_width()
        height = self._board_canvas.winfo_height()

        row_delta = height / self.row_number
        column_delta = width / self.column_number

        # Creates a Disc object according to the user's move
        # and gets the zero based row number and column number
        # of the clicked disc on the board
        move_disc = othello_disc.from_pixel(event.y, event.x, row_delta, column_delta, self._current_state.turn)
        row_move, column_move = move_disc.row_index, move_disc.column_index

        try:
            self._current_state.move(row_move, column_move)
                        
            self._black_score_text.set('BLACK DISC:  {}'.format(self._current_state.disc_number(othello_game_logic.BLACK)))
            self._white_score_text.set('WHITE DISC:  {}'.format(self._current_state.disc_number(othello_game_logic.WHITE)))
            
            self._instruction_text.set('\nTurn: {}'.format(
                self._color_reference_dict[self._current_state.turn]))

            # Checks if the game or the round is
            # over, everytime after the player makes
            # a valid move
            self._current_state.check_game_over()
            self._current_state.check_round_over()

        # InvalidMoveError is raised, whenever the user makes
        # an invalid move. Show a tip to the user to let him know
        # he makes an invalid move
        except othello_game_logic.InvalidMoveError:
            self._instruction_text.set('You made an invalid move!\nTurn: {}'.format(
                self._color_reference_dict[self._current_state.turn]))

        except othello_game_logic.RoundOverError:
            self._instruction_text.set('Turn: {}'.format(
                self._color_reference_dict[self._current_state.turn]))

        except othello_game_logic.GameOverError:
            winner_number = self._current_state.game_winner(self.winning_way)
            self._instruction_text.set(self._winner_reference_dict[winner_number])

            self._show_final_option_frame()

        # Finally redraws the game board
        # and all of the discs on the game board
        finally:
            self._redraw_game_board()
        
        
    def _redraw_game_board(self) -> None:
        """
        Deletes and redraws the game board and all of the discs. Draw the disc
        by get the pixel coordinate of top-left corner point and bottom-right
        corner point of the bounding cell around the disc
        """
        self._board_canvas.delete(tkinter.ALL)
        
        canvas_width = self._board_canvas.winfo_width()
        canvas_height = self._board_canvas.winfo_height()

        # Gets the width of each row and the height of each column
        # on the othello game board, by dividing the canvas width and
        # height by the row number and column number, respectively
        row_delta = canvas_height / self.row_number
        column_delta = canvas_width / self.column_number

        disc_reference_dict = {othello_game_logic.BLACK: 'black',
                               othello_game_logic.WHITE: 'white'}

        # Draws the othello game board
        # Draws row lines on the game board canvas
        for row_index in range(0, self.row_number + 1):
            
            self._board_canvas.create_line(0, row_delta * row_index,
                                           canvas_width, row_delta * row_index)

        # Draws column lines on the game board canvas
        for column_index in range(0, self.column_number + 1):
            
            self._board_canvas.create_line(column_delta * column_index, 0,
                                           column_delta * column_index, canvas_height)

        # Draws all of the discs on the game board
        # by scanning the game state (nested list)
        # of the othello
        for row_index in range(len(self._current_state.state)):
            for column_index in range(len(self._current_state.state[row_index])):

                # Assign a symbol disc number to a variable                               
                disc = self._current_state.state[row_index][column_index]

                # Checks if the cell has a disc to draw
                if disc != othello_game_logic.NONE:

                    # Gets the pixel coordinate of the top-left and bottom-right corner of
                    # the bounding cell around the disc. Leave a space between the disc and
                    # and the cell to make the disc look nicer (by adding 0.03 and 0.97, rather than 1)
                    topleft_x1, topleft_y1 = (column_index + 0.03) * column_delta, (row_index + 0.03) * row_delta
                    bottomright_x2, bottomright_y2 = (column_index + 0.97) * column_delta, (row_index + 0.97) * row_delta

                    # Draws the disc, filled in corresponding color
                    self._board_canvas.create_oval(topleft_x1, topleft_y1, bottomright_x2, bottomright_y2,
                                                   fill = disc_reference_dict[disc], width = 0)


    def _show_final_option_frame(self) -> None:
        """
        Shows the final option frame after the game is finished
        Gives the user a choice to choose whether to play again
        or return to main menu. The user can also just dismiss
        the window
        """
        # FINAL OPTION FRAME
        self._final_option_frame = tkinter.Frame(master = self._game_board_frame, bg = '#ffffb3')
        
        self._final_option_frame.grid(
            row = 2, column = 1, columnspan = 2,
            padx = 10, pady = 10, sticky = tkinter.S + tkinter.E)

        # PLAY AGAIN BUTTON
        play_again_button = tkinter.Button(
            master = self._final_option_frame, text = 'Play Again',
            font = ('Helvatica', 14), command = self._on_start)

        play_again_button.grid(row = 0, column = 0, padx = 10, pady = 3)

        # RETURN TO MAIN MENU BUTTON
        return_button = tkinter.Button(
            master = self._final_option_frame, text = 'Return To Main Menu',
            font = ('Helvatica', 14), command = self._return_menu)

        return_button.grid(row = 0, column = 1, padx = 10, pady = 3)


    def _return_menu(self) -> None:
        """
        Called whenever the user clicks the Return To Main Menu button.
        Hide the final option frame and show the main menu frame. In addition,
        show the RESUME button in the main menu frame in the main window.
        """
        # After the user click the Return To Main
        # Menu Button, hides the final option frame
        # and shows the main menu frame
        self._final_option_frame.grid_forget()
        self._show_main_menu_frame()

        # RESUME BUTTON
        self._resume_button = tkinter.Button(
            master = self._main_menu_frame, text = 'RESUME',
            font = _DEFAULT_FONT, command = self._on_start)

        self._resume_button.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N)



# Runs Othello game application
if __name__ == '__main__':
    OthelloApplication().start()
