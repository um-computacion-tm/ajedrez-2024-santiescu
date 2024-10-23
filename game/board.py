from game.rook import Rook 
from game.pawn import Pawn
from game.bishop import Bishop
from game.king import King
from game.knight import Knight
from game.queen import Queen
from game.exceptions import OutOfBoard, RowOutOfBoard, ColumnOutOfBoard
from game.exceptions import GameOverException, NonCaptureOwnPieceError, NonPassOverPieceError, NonCaptureForwardError, NonPieceOriginError
from game.pieces import Piece
class Board: 
    def __init__(self):  
        self.__positions__ = [[None] * 8 for _ in range(8)]
        self.starting_positions()
    
    def get_piece(self,row,col):
        return self.__positions__[row][col]
    
    def get_piece_color(self, row, col):
        piece = self.get_piece(row, col)
        if piece is None:
            raise NonPieceOriginError(f"There is no piece at the origin position.")
        return piece.get_color()
    
    def is_valid_move(self, from_row, from_col, to_row, to_col):
        piece = self.get_piece(from_row, from_col)
        if not piece:
            return False

        posibles_movimientos = piece.possible_moves(from_row, from_col)
        return (to_row, to_col) in posibles_movimientos

    
    def move(self, from_row, from_col, to_row, to_col):
        self.validate_position(from_row, from_col)
        self.validate_position(to_row, to_col)
        origin = self.get_piece(from_row, from_col)
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)
    
    def starting_positions(self):

        for i in range(8):
            self.__positions__[1][i] = Pawn("BLACK")
            self.__positions__[6][i] = Pawn("WHITE")

        self.__positions__[0][0] = Rook("BLACK")
        self.__positions__[0][7] = Rook("BLACK")
        self.__positions__[7][7] = Rook("WHITE")
        self.__positions__[7][0] = Rook("WHITE")

        self.__positions__[0][1] = Knight("BLACK")
        self.__positions__[0][6] = Knight("BLACK")
        self.__positions__[7][1] = Knight("WHITE")
        self.__positions__[7][6] = Knight("WHITE")

        self.__positions__[0][2] = Bishop("BLACK")
        self.__positions__[0][5] = Bishop("BLACK")
        self.__positions__[7][2] = Bishop("WHITE")
        self.__positions__[7][5] = Bishop("WHITE")

        self.__positions__[0][3] = Queen("BLACK")
        self.__positions__[7][3] = Queen("WHITE")

        self.__positions__[0][4] = King("BLACK")
        self.__positions__[7][4] = King("WHITE")

    def get_board_state(self):
        board_repr = []
        for row in self.__positions__:
            row_repr = [str(piece) if piece else '.' for piece in row]
            board_repr.append(row_repr)
        return board_repr
    
    def move_piece(self, from_row, from_col, to_row, to_col):
        # Mueve una pieza en el tablero si las reglas del juego lo permiten.
        piece = self.get_piece(from_row, from_col)
        target_piece = self.get_piece(to_row, to_col)

        if not piece:
            raise ValueError("No hay ninguna pieza en la posición de origen")

        if target_piece and piece.get_color() == target_piece.get_color():
            raise NonCaptureOwnPieceError("No puedes capturar tus propias piezas")

        if not self._ruta_despejada(from_row, from_col, to_row, to_col):
            raise NonPassOverPieceError("No puedes saltar sobre otras piezas")

        if isinstance(piece, Pawn):
            if not self._es_movimiento_valido_peon(from_row, from_col, to_row, to_col, target_piece):
                raise NonCaptureForwardError("Un peón no puede capturar hacia adelante")

        self._make_move(from_row, from_col, to_row, to_col)
        self._validate_end_game()

    def _ruta_despejada(self, from_row, from_col, to_row, to_col):
        if isinstance(self.__positions__[from_row][from_col], Knight):
            return True  

        fila_paso = 1 if to_row > from_row else -1 if to_row < from_row else 0
        columna_paso = 1 if to_col > from_col else -1 if to_col < from_col else 0

        fila_actual, columna_actual = from_row + fila_paso, from_col + columna_paso
        while fila_actual != to_row or columna_actual != to_col:
            if self.__positions__[fila_actual][columna_actual]:
                return False
            fila_actual += fila_paso
            columna_actual += columna_paso
        return True
    
    def _es_movimiento_valido_peon(self, from_row, from_col, to_row, to_col, target_piece):
        direccion = 1 if self.__positions__[from_row][from_col].get_color() == 'BLACK' else -1
        return not (to_row == from_row + direccion and target_piece is not None and from_col == to_col)

    def _make_move(self, from_row, from_col, to_row, to_col):
        self.__positions__[to_row][to_col] = self.__positions__[from_row][from_col]
        self.__positions__[from_row][from_col] = None


    def _validate_end_game(self):
        piezas_blancas, piezas_negras = 0, 0
        for fila in self.__positions__:
            for pieza in fila:
                if pieza:
                    if pieza.get_color() == 'WHITE':
                        piezas_blancas += 1
                    elif pieza.get_color() == 'BLACK':
                        piezas_negras += 1

        if piezas_negras == 0:
            raise GameOverException("White wins")
        elif piezas_blancas == 0:
            raise GameOverException("Black wins")
