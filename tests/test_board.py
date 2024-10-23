import unittest
from game.board import Board
from game.exceptions import NonCaptureOwnPieceError, NonPassOverPieceError, GameOverException

class TestTablero(unittest.TestCase):
    def test_movimiento_invalido_sin_pieza(self):
        tablero = Board()
        self.assertFalse(tablero.is_valid_move(3, 3, 4, 4))

    def test_intento_captura_propia_pieza(self):
        tablero = Board()
        tablero.board = [[None for _ in range(8)] for _ in range(8)]
        tablero.board[7][0] = 'R'
        tablero.board[6][0] = 'P'
        with self.assertRaises(NonCaptureOwnPieceError) as contexto:
            tablero.move_piece(7, 0, 6, 0)
        self.assertEqual(str(contexto.exception), "No puedes capturar tus propias piezas.")

    def test_pieza_pasa_sobre_otras(self):
        tablero = Board()
        tablero.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        tablero.__positions__[0][0] = 'R'
        tablero.__positions__[0][1] = 'P'
        with self.assertRaises(NonPassOverPieceError) as contexto:
            tablero.move_piece(0, 0, 0, 2)
        self.assertEqual(str(contexto.exception), "No puedes pasar por encima de tus propias piezas.")

    def test_partida_finalizada_gana_blancas(self):
        tablero = Board()
        class Torre:
            def get_color(self):
                return 'WHITE'
        tablero.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        tablero.__positions__[7][7] = Torre()
        with self.assertRaises(GameOverException) as contexto:
            tablero._validate_end_game()
        self.assertEqual(str(contexto.exception), "White wins")

    def test_partida_finalizada_gana_negras(self):
        tablero = Board()
        class Torre:
            def get_color(self):
                return 'BLACK'
        tablero.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        tablero.__positions__[0][0] = Torre()
        with self.assertRaises(GameOverException) as contexto:
            tablero._validate_end_game()
        self.assertEqual(str(contexto.exception), "Black wins")

if __name__ == '__main__':
    unittest.main()
