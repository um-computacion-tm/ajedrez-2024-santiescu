class Piece: 
    def __init__ (self, color):
        self.__color__ = color 
    def get_color(self):
        return self.__color__

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.color = color
        self.name = 'Knight'

    def __str__(self):
        return "N" if self.color == "WHITE" else "n"

    def possible_moves(self, current_position, board):
        moves = []
        row, col = current_position
        move_offsets = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        
        for offset in move_offsets:
            new_row = row + offset[0]
            new_col = col + offset[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:  # Dentro del tablero
                piece = board.get_piece(new_row, new_col)
                if piece is None or piece.get_color() != self.get_color():
                    moves.append((new_row, new_col))
        
        return moves