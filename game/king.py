from game.pieces import Piece

class King(Piece):
    white_str = "♔"
    black_str = "♚"

    def __str__(self):
        return '♔' if self.__color__ == 'WHITE' else '♚'

    def possible_moves(self, from_row, from_col):
        directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
        return super().possible_moves_gen(from_row, from_col, directions, one_step=True)
