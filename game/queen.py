from game.pieces import Piece

class Queen(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.__queen_king_directions__ = [(-1,0),(1,0),(0,-1),(0,1)]+[(-1,-1),(-1,1),(1,-1),(1,1)]

    def __str__(self):
        return '♕' if self.__color__ == 'WHITE' else '♛'


    def possible_moves(self, from_row, from_col):
        directions = self.__queen_king_directions__
        return super().possible_moves_gen(from_row, from_col, directions)