from pieces import Piece

class Rook(Piece):
    white_str = "♜"
    black_str = "♖"

    def possible_positions_vd(self, row, col):
        possibles = []
        for next_row in range(row + 1, 8):

            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, col))
                break
            possibles.append((next_row, col))
        return possibles

    def possible_positions_va(self, row, col):
        possibles = []
        for next_row in range(row - 1, -1, -1):
            possibles.append((next_row, col))
        return possibles
    
 