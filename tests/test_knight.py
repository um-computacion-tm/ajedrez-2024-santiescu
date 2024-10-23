import unittest
from game.knight import Knight

class TestCaballero(unittest.TestCase):
    def test_convertir_a_str(self):
        caballero_blanco = Knight('WHITE')
        caballero_negro = Knight('BLACK')
        self.assertEqual(str(caballero_blanco), '♘')
        self.assertEqual(str(caballero_negro), '♞')
        
    def test_generar_direcciones_caballero(self):
        caballero = Knight('WHITE')
        direcciones_correctas = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        self.assertEqual(caballero.generate_knight_directions(), direcciones_correctas)

if __name__ == '__main__':
    unittest.main()
