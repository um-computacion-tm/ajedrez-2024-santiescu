import unittest
from game.pieces import Piece

class VerificacionPieza(unittest.TestCase):
    def test_color_pieza_blanca(self):
        color_blanco = 'WHITE'
        pieza_blanca = Piece(color_blanco)
        self.assertEqual(pieza_blanca.__color__, color_blanco)

    def test_color_pieza_negra(self):
        color_negro = 'BLACK'
        pieza_negra = Piece(color_negro)
        self.assertEqual(pieza_negra.__color__, color_negro)

    def test_obtener_color_pieza_blanca(self):
        pieza = Piece("WHITE")
        self.assertEqual(pieza.get_color(), "WHITE")
    
    def test_obtener_color_pieza_negra(self):
        pieza = Piece("BLACK")
        self.assertEqual(pieza.get_color(), "BLACK")

if __name__ == '__main__':
    unittest.main()
