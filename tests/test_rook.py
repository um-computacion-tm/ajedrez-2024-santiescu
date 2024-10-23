import unittest
from game.rook import Rook
from game.board import Board
from game.pawn import Pawn

class TestRook(unittest.TestCase):

    def test_str(self):
        board = Board()
        rook = Rook("WHITE", board)
        self.assertEqual(str(rook), "♖")  # El símbolo para la torre blanca es ♖.

    def test_move_vertical_desc(self):
        board = Board()
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)  # Colocamos la torre en el tablero en la posición inicial.
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(possibles, [(5, 1), (6, 1), (7, 1)])  # Movimientos válidos hacia abajo.

    def test_move_vertical_asc(self):
        board = Board()
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)  # Colocamos la torre en el tablero en la posición inicial.
        possibles = rook.possible_positions_va(4, 1)
        self.assertEqual(possibles, [(3, 1), (2, 1), (1, 1), (0, 1)])  # Movimientos válidos hacia arriba.

    def test_move_vertical_desc_with_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("WHITE", board))  # Colocamos un peón blanco en la trayectoria.
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)  # Colocamos la torre en el tablero.
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(possibles, [(5, 1)])  # La torre no debe saltar ni capturar piezas del mismo color.

    def test_move_vertical_desc_with_not_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("BLACK", board))  # Colocamos un peón negro en la trayectoria.
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)  # Colocamos la torre en el tablero.
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(possibles, [(5, 1), (6, 1)])  # La torre puede capturar la pieza enemiga.

    def test_move_horizontal_right(self):
        board = Board()
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)  # Colocamos la torre en la posición inicial.
        possibles = rook.possible_positions_hr(4, 1)  # Movimientos horizontales a la derecha.
        self.assertEqual(possibles, [(4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7)])  # Movimientos válidos.

    def test_move_horizontal_left(self):
        board = Board()
        rook = Rook("WHITE", board)
        board.set_piece(4, 4, rook)  # Colocamos la torre en la posición inicial.
        possibles = rook.possible_positions_hl(4, 4)  # Movimientos horizontales a la izquierda.
        self.assertEqual(possibles, [(4, 3), (4, 2), (4, 1), (4, 0)])  # Movimientos válidos.

    def test_move_horizontal_right_with_own_piece(self):
        board = Board()
        board.set_piece(4, 3, Pawn("WHITE", board))  # Colocamos un peón blanco en la trayectoria.
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)  # Colocamos la torre en el tablero.
        possibles = rook.possible_positions_hr(4, 1)
        self.assertEqual(possibles, [(4, 2)])  # La torre no debe saltar ni capturar piezas del mismo color.

    def test_move_horizontal_right_with_not_own_piece(self):
        board = Board()
        board.set_piece(4, 3, Pawn("BLACK", board))  # Colocamos un peón negro en la trayectoria.
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)  # Colocamos la torre en el tablero.
        possibles = rook.possible_positions_hr(4, 1)
        self.assertEqual(possibles, [(4, 2), (4, 3)])  # La torre puede capturar la pieza enemiga.

    def test_move_diagonal(self):
        board = Board()
        rook = Rook("WHITE", board)
        board.set_piece(0, 0, rook)  # Colocamos la torre en la esquina del tablero.
        is_possible = rook.valid_positions(0, 0, 1, 1)  # Intentamos mover la torre diagonalmente.
        self.assertFalse(is_possible)  # Las torres no pueden moverse en diagonal.

if __name__ == "__main__":
    unittest.main()