class Piece:
    def __init__(self, color, board):
        self.__color__ = color
        self.__board__ = board

    def __str__(self):
        if self.__color__ == "WHITE":
            return self.white_str
        else:
            return self.black_str
        
    def get_color(self):
        return self.__color__

    
    def is_row_col_in_valid_positions(self,to_row,to_col,possible_positions):
        if (to_row,to_col) in possible_positions:
            return True
        else: False
        
            
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
        self.white_str = "♘"  
        self.black_str = "♞"  

    def is_valid_piece_move(self, board, from_row, from_col, to_row, to_col):
        return (abs(from_row - to_row) == 2 and abs(from_col - to_col) == 1) or \
               (abs(from_row - to_row) == 1 and abs(from_col - to_col) == 2)