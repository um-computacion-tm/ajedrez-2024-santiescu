from pieces import Piece

class Rook(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)  # Inicializar color y tablero
        self.white_str = "♖"
        self.black_str = "♜"

    def __str__(self):
        return self.white_str if self.color == "WHITE" else self.black_str

    def possible_positions_vd(self, row, col):
        """Movimientos verticales hacia abajo"""
        positions = []
        for r in range(row + 1, 8):  # Mueve hacia abajo en las filas
            other_piece = self.board.get_piece(r, col)
            if other_piece is None:
                positions.append((r, col))
            else:
                if other_piece.color != self.color:
                    positions.append((r, col))  # Puede capturar la pieza enemiga
                break
        return positions

    def possible_positions_va(self, row, col):
        """Movimientos verticales hacia arriba"""
        positions = []
        for r in range(row - 1, -1, -1):  # Mueve hacia arriba en las filas
            other_piece = self.board.get_piece(r, col)
            if other_piece is None:
                positions.append((r, col))
            else:
                if other_piece.color != self.color:
                    positions.append((r, col))  # Puede capturar la pieza enemiga
                break
        return positions

    def possible_positions_hr(self, row, col):
        """Movimientos horizontales hacia la derecha"""
        positions = []
        for c in range(col + 1, 8):  # Mueve hacia la derecha en las columnas
            other_piece = self.board.get_piece(row, c)
            if other_piece is None:
                positions.append((row, c))
            else:
                if other_piece.color != self.color:
                    positions.append((row, c))  # Puede capturar la pieza enemiga
                break
        return positions

    def possible_positions_hl(self, row, col):
        """Movimientos horizontales hacia la izquierda"""
        positions = []
        for c in range(col - 1, -1, -1):  # Mueve hacia la izquierda en las columnas
            other_piece = self.board.get_piece(row, c)
            if other_piece is None:
                positions.append((row, c))
            else:
                if other_piece.color != self.color:
                    positions.append((row, c))  # Puede capturar la pieza enemiga
                break
        return positions

    def valid_positions(self, start_row, start_col, end_row, end_col):
        """Verifica si el movimiento de la torre es válido (horizontal o vertical)"""
        if start_row == end_row or start_col == end_col:
            return True  # Movimiento válido en línea recta
        return False  # Las torres no pueden moverse en diagonal
    
    def is_row_col_in_valid_postions(self,to_row,to_col,possible_positions):
        if (to_row,to_col) in possible_positions:
            return True
        else: False
