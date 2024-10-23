from game.pieces import Piece
class Knight(Piece):
    # def __init__(self, color, board):
    #     super().__init__(color, board)
    #     self.white_str = "♘"  # Símbolo para el caballo blanco
    #     self.black_str = "♞"  # Símbolo para el caballo negro

    def __str__(self):
        return '♘' if self.__color__ == 'WHITE' else '♞'
    
    def generate_knight_directions(self):
        directions = []
        moves = [2, 1, -1, -2]
        for i in moves:
            for j in moves:
                if abs(i) != abs(j):
                    directions.append((i, j))
        return directions

    def possible_moves(self, from_row, from_col):

        directions = self.generate_knight_directions()
        return self.possible_moves_gen(from_row, from_col, directions)
