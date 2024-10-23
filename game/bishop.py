from game.pieces import Piece

class Bishop(Piece):
    white_str = "♗"
    black_str = "♝"

    def __str__(self):
                
        return '♗' if self.__color__ == 'WHITE' else '♝'

    def possible_moves(self, from_row, from_col):
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  
        return self.possible_moves_gen(from_row, from_col, directions)