from pieces import Piece
from exceptions import OutOfBoard
class Knight(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)
        self.white_str = "♘"  # Símbolo para el caballo blanco
        self.black_str = "♞"  # Símbolo para el caballo negro

    def is_valid_piece_move(self, board, from_row, from_col, to_row, to_col):
        """Verifica si el movimiento es válido para el caballo."""
        if not self.is_within_bounds(to_row, to_col):
            raise OutOfBoard(f"Posición fuera del tablero: {to_row}, {to_col}")
        
        # El caballo se mueve en forma de "L"
        return (abs(from_row - to_row) == 2 and abs(from_col - to_col) == 1) or \
               (abs(from_row - to_row) == 1 and abs(from_col - to_col) == 2)

    def possible_positions(self, row, col):
        """Devuelve una lista de posiciones válidas a las que el caballo puede moverse."""
        # Todas las posibles combinaciones de movimientos del caballo
        moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        possible_moves = []
        for move in moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if self.is_within_bounds(new_row, new_col):
                possible_moves.append((new_row, new_col))
        return possible_moves

    def is_within_bounds(self, row, col):
        """Verifica si la posición está dentro de los límites del tablero."""
        return 0 <= row < 8 and 0 <= col < 8