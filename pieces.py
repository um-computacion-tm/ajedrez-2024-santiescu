class Piece:
    def __init__(self, color, board):
        self.__color__ = color
        self.__board__ = board

    def __str__(self):
        if self.__color__ == "WHITE":
            return self.white_str
        else:
            return self.black_str
        
class Pawn(Piece):
    def __init__(self,color,board):
        super().__init__(color,board)
    
    def __str__(self):
        if self.__color__=="WHITE":
            return "♟"
        else: return "♙"

class Knight(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)
        self.white_str = "♘"  # Símbolo para el caballo blanco
        self.black_str = "♞"  # Símbolo para el caballo negro

    def is_valid_piece_move(self, board, from_row, from_col, to_row, to_col):
        """Verifica si el movimiento es válido para el caballo."""
        # El caballo se mueve en forma de "L"
        return (abs(from_row - to_row) == 2 and abs(from_col - to_col) == 1) or \
               (abs(from_row - to_row) == 1 and abs(from_col - to_col) == 2)