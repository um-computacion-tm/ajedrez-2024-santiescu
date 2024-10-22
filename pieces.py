class Piece:
    
    def __init__(self, color):
        self.__color__ = color
        self.__dir_king_queen__ = [(-1,0),(1,0),(0,-1),(0,1)]+[(-1,-1),(-1,1),(1,-1),(1,1)]

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

    def treid(self):
        return True