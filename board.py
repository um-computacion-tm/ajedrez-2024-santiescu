from rook import Rook 
class Board: 
    def __init__ (self): 
        self.__positions__ = []
        for _ in range (8):
            col = []
            for _ in range (8):
                col.append(None)
            self.__positions__.append(col)
        self.__positions__ [0][0] = Rook ("BLACK")
        self.__positions__ [0][7] = Rook ("BLACK")
        self.__positions__ [7][7] = Rook ("WHITE")
        self.__positions__ [7][0] = Rook ("WHITE")
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        self.__positions__[0][0] = Rook("BLACK", self)

    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
            board_str += "\n"
        return board_str

    def get_piece(self, row, col):
        return self.__positions__ [row][col]
    
    def set_piece(self, row, col, piece):

        self.__positions__[row][col] = piece
    


  