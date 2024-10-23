from game.rook import Rook 
from game.pawn import Pawn
from game.bishop import Bishop
from game.king import King
from game.knight import Knight
from game.queen import Queen
from game.exceptions import OutOfBoard, RowOutOfBoard, ColumnOutOfBoard

class Board: 
    def __init__(self, for_test=False): 
         
        self._positions_ = [[None] * 8 for _ in range(8)]
        self.starting_positions()

    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell) + " "
                else:
                    board_str += ". " 
            board_str += "\n"
        return board_str.strip()
    
    def get_piece(self,row,col):
        if not 0 <= row < 8 and not 0 <= col < 8:
            raise OutOfBoard()
        elif not 0 <= row < 8:
            raise RowOutOfBoard()
        elif not 0 <= col < 8:
            raise ColumnOutOfBoard()
        else: return self.__positions__[row][col]
    
    def set_piece(self, row, col, piece):
        if not (0 <= row < 8 or 0 <= col < 8):
            raise OutOfBoard()
        elif not 0 <= row < 8:
            raise RowOutOfBoard()
        elif not 0 <= col < 8:
            raise ColumnOutOfBoard()
        else: self.__positions__[row][col] = piece
    
    def move(self, from_row, from_col, to_row, to_col):
        self.validate_position(from_row, from_col)
        self.validate_position(to_row, to_col)
        origin = self.get_piece(from_row, from_col)
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)
    
    def starting_positions(self):

        for i in range(8):
            self.__positions__[1][i] = Pawn("BLACK")
            self.__positions__[6][i] = Pawn("WHITE")

        self.__positions__[0][0] = Rook("BLACK", self)
        self.__positions__[0][7] = Rook("BLACK", self)
        self.__positions__[7][7] = Rook("WHITE", self)
        self.__positions__[7][0] = Rook("WHITE", self)

        self.__positions__[0][1] = Knight("BLACK")
        self.__positions__[0][6] = Knight("BLACK")
        self.__positions__[7][1] = Knight("WHITE")
        self.__positions__[7][6] = Knight("WHITE")

        self.__positions__[0][2] = Bishop("BLACK")
        self.__positions__[0][5] = Bishop("BLACK")
        self.__positions__[7][2] = Bishop("WHITE")
        self.__positions__[7][5] = Bishop("WHITE")

        self.__positions__[0][3] = Queen("BLACK")
        self.__positions__[7][3] = Queen("WHITE")

        self.__positions__[0][4] = King("BLACK")
        self.__positions__[7][4] = King("WHITE")

    def get_board_state(self):
        board_repr = []
        for row in self.__positions__:
            row_repr = [str(piece) if piece else '.' for piece in row]
            board_repr.append(row_repr)
        return board_repr
