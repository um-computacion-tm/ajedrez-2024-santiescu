from board import Board
from exceptions import InvalidMove
class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
    
    def is_playing(self):
        return True
    
    def move(
        self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):
        # validate coords
        piece = self.__board__.get_piece(from_row, from_col)
        if piece.valid_positions(from_row, from_col, to_row, to_col):
            raise InvalidMove()
        self.change_turn()

    def turn(self):
        return self.__turn__
    
    def show_board(self):
        return str(self.__board__)

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"