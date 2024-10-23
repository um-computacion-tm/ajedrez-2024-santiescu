from game.pieces import Piece, king_queen_mov

class Queen(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.__queen_king_directions__ = king_queen_mov
    def __str__(self):
        return '♕' if self.__color__ == 'WHITE' else '♛'


    def possible_moves(self, from_row, from_col):
        directions = self.__queen_king_directions__
        return super().possible_moves_gen(from_row, from_col, directions)