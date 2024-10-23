class InvalidMove(Exception):
    message = "Movimiento de pieza invalido"
    
    def __str__(self):
        return self.message
    
class NonCaptureOwnPieceError(InvalidMove):
    message = "No puedes capturar tus propias piezas."

class NonPassOverPieceError(InvalidMove):
    message = "No puedes pasar por encima de tus propias piezas."

class NonCaptureForwardError(InvalidMove):
    message = "No puedes capturar hacia adelante."

class InvalidTurn(InvalidMove):
    message = "No puedes mover pieza de otro jugador"

class EmptyPosition(InvalidMove):
    message = "La posicion esta vacia"

class WrongTurnError(InvalidMove):
    message = "No es el turno de la pieza seleccionada."

class InvalidPieceMoveError(InvalidMove):
    message = "Movimiento no válido para la pieza seleccionada."

class NonPieceOriginError(InvalidMove):
    message = "No hay ninguna pieza en la posición de origen."


class OutOfBoard(InvalidMove):
    message = "La posicion indicada se encuentra fuera del tablero"

class RowOutOfBoard(OutOfBoard):
    message = "La posicion indicada se encuentra fuera del tablero"  # Unificar mensaje

class ColumnOutOfBoard(OutOfBoard):
    message = "La posicion indicada se encuentra fuera del tablero"  # Unificar mensaje

class GameOverException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)
class OutOfBoundsError(InvalidMove):
    message = "Los valores de fila y columna deben estar entre 0 y 7."

class NonNumericInputError(InvalidMove):
    message = "Debes ingresar valores numéricos entre 0 y 7.."


class GameOverException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

