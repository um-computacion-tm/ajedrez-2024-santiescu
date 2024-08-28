class Piece: 
    def __init__ (self, color):
        self.__color__ = color 
    def get_color(self):
        return self.__color__

class Rook(Piece):
    white_str='W'
    black_str='B'

    def possible_positions(self,row,col):
        possibles=[]
        for next_row in range(row+1,8):
            if self.board.get_piece[next_row][col] is None:
                possibles.append((next_row,col))
        return possibles