from game.pieces import Piece

class Pawn(Piece):
    def __str__(self):

        return '♙' if self.__color__ == 'WHITE' else '♟'
    
    def possible_moves(self, row, col):
        moves = []
        direction = -1 if self.__color__ == 'WHITE' else 1
        start_row = 6 if self.__color__ == 'WHITE' else 1

        moves.append((row + direction, col))
        
        if row == start_row:
            moves.append((row + 2 * direction, col))

        if row != start_row:  
            moves.append((row + direction, col - 1))
            moves.append((row + direction, col + 1))
        return moves

    def treid(self):
        return True