from game.board import Board
from game.exceptions import InvalidMove, NonPieceOriginError, WrongTurnError, InvalidPieceMoveError, GameOverException

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
    
    def is_playing(self):
        return True
    
    def get_board (self):
        return self.__board__.get_board_state()
    
    def move(
        self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):
        try:
            # Obtener el color de la pieza en la posición de origen
            color_pieza = self.__board__.get_piece_color(from_row, from_col)
            if color_pieza is None:
                raise NonPieceOriginError()
            
            # Verificar que la pieza sea del jugador con el turno actual
            if color_pieza != self.__turn__:
                raise WrongTurnError()
            
            # Verificar que el movimiento sea válido y realizarlo
            if not self.__board__.is_valid_move(from_row, from_col, to_row, to_col):
                raise InvalidPieceMoveError()
            
            self.__board__.move_piece(from_row, from_col, to_row, to_col)
            
            # Cambiar el turno después de mover
            self.cambiar_turno()    

        except GameOverException as e:
            raise e 

    @property
    def turn(self):
        return self.__turn__
    
    def show_board(self):
        return str(self.__board__)

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"