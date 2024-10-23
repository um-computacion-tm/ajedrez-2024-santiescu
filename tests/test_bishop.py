import unittest
from game.bishop import Bishop

class VerificarAlfil(unittest.TestCase):

    def test_representacion_str(self):
        alfil_blanco = Bishop('WHITE')
        alfil_negro = Bishop('BLACK')
        self.assertEqual(str(alfil_blanco), '♗')
        self.assertEqual(str(alfil_negro), '♝')

    def test_movimientos_disponibles_blanco(self):
        alfil = Bishop('WHITE')
        movimientos_esperados = [
            (2, 2), (1, 1), (0, 0),  # Diagonal superior izquierda
            (2, 4), (1, 5), (0, 6),  # Diagonal superior derecha
            (4, 2), (5, 1), (6, 0),  # Diagonal inferior izquierda
            (4, 4), (5, 5), (6, 6), (7, 7)  # Diagonal inferior derecha
        ]
        self.assertEqual(alfil.possible_moves(3, 3), movimientos_esperados)

    def test_movimientos_disponibles_negro(self):
        alfil = Bishop('BLACK')
        movimientos_esperados = [
            (2, 2), (1, 1), (0, 0),  # Diagonal superior izquierda
            (2, 4), (1, 5), (0, 6),  # Diagonal superior derecha
            (4, 2), (5, 1), (6, 0),  # Diagonal inferior izquierda
            (4, 4), (5, 5), (6, 6), (7, 7)  # Diagonal inferior derecha
        ]
        self.assertEqual(alfil.possible_moves(3, 3), movimientos_esperados)

if __name__ == '__main__':
    unittest.main()
