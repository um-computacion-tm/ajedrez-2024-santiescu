class InvalidMove(Exception):
    message = "Movimiento de pieza invalido"
    
    def __str__(self):
        return self.message
    
class InvalidMoveNoPiece(InvalidMove):
    ...

class InvalidMoveRookMove(InvalidMove):
    ...

class InvalidTurn(InvalidMove):
    message = "No puedes mover pieza de otro jugador"

class EmptyPosition(InvalidMove):
    message = "La posicion esta vacia"

class OutOfBoard(InvalidMove):
    message = "La posicion indicada se encuentra fuera del tablero"

class RowOutOfBoard(OutOfBoard):
    message = "La posicion indicada se encuentra fuera del tablero"  # Unificar mensaje

class ColumnOutOfBoard(OutOfBoard):
    message = "La posicion indicada se encuentra fuera del tablero"  # Unificar mensaje
