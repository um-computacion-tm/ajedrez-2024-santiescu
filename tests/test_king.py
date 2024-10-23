import unittest
from game.king import King

class TestRey(unittest.TestCase):
    def test_representacion_str(self):
        rey_blanco = King('WHITE')
        rey_negro = King('BLACK')
        self.assertEqual(rey_blanco.__str__(), '♔')
        self.assertEqual(rey_negro.__str__(), '♚')


    def test_movimientos_rey_blanco(self):
        rey = King('WHITE')
        fila, columna = 4, 4
        movimientos_esperados = [(5, 4), (4, 5), (3, 4), (4, 3), (5, 5), (3, 5), (5, 3), (3, 3)]
        movimientos = rey.possible_moves(fila, columna)
        self.assertCountEqual(movimientos, movimientos_esperados)


    def test_movimientos_rey_negro(self):
        rey = King('BLACK')
        fila, columna = 4, 4
        movimientos_esperados = [(5, 4), (4, 5), (3, 4), (4, 3), (5, 5), (3, 5), (5, 3), (3, 3)]
        movimientos = rey.possible_moves(fila, columna)
        self.assertCountEqual(movimientos, movimientos_esperados)

if __name__ == '__main__':
    unittest.main()
