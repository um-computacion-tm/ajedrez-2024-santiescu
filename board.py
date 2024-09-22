from rook import Rook 
from pawn import Pawn

class Board: 
    def __init__ (self): 
        self.__positions__ = []
        for _ in range (8):
            col = []
            for _ in range (8):
                col.append(None)
            self.__positions__.append(col)

    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell) + " "  # Asegúrate de agregar un espacio
                else:
                    board_str += ". "  # Cambié a punto para representar celdas vacías
            board_str += "\n"
        return board_str.strip()  # Eliminar el último salto de línea

    def get_piece(self, row, col):
        return self.__positions__[row][col]
    
    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece
    
    def rook_positions(self): 
        self.__positions__[0][0] = Rook("BLACK", self)
        self.__positions__[0][7] = Rook("BLACK", self)
        self.__positions__[7][7] = Rook("WHITE", self)
        self.__positions__[7][0] = Rook("WHITE", self)

    def move(self, from_row, from_col, to_row, to_col):
        origin = self.get_piece(from_row, from_col)
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)
    
    def pawn_positions(self):
        self.__positions__[1][0] = Pawn("BLACK", self)
        self.__positions__[1][1] = Pawn("BLACK", self)
        self.__positions__[1][2] = Pawn("BLACK", self)
        self.__positions__[1][3] = Pawn("BLACK", self)
        self.__positions__[1][4] = Pawn("BLACK", self)
        self.__positions__[1][5] = Pawn("BLACK", self)
        self.__positions__[1][6] = Pawn("BLACK", self)
        self.__positions__[1][7] = Pawn("BLACK", self)          
        self.__positions__[6][0] = Pawn("WHITE", self)
        self.__positions__[6][1] = Pawn("WHITE", self)
        self.__positions__[6][2] = Pawn("WHITE", self)
        self.__positions__[6][3] = Pawn("WHITE", self)
        self.__positions__[6][4] = Pawn("WHITE", self)
        self.__positions__[6][5] = Pawn("WHITE", self)
        self.__positions__[6][6] = Pawn("WHITE", self)
        self.__positions__[6][7] = Pawn("WHITE", self)