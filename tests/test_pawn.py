import unittest
from game.pawn import Pawn

class VerificarPeon(unittest.TestCase):

# Verifica que el método __str__ del Peón devuelva 'P' para un peón blanco y 'p' para uno negro.
    def test_metodo_str(self):
        peon_blanco = Pawn('WHITE')
        peon_negro = Pawn('BLACK')
        self.assertEqual(str(peon_blanco), '♙')
        self.assertEqual(str(peon_negro), '♟')

# Evalúa los posibles movimientos del peón blanco desde varias posiciones. Llama al método possible_moves con diferentes posiciones iniciales y compara los movimientos obtenidos
    def test_movimientos_peon_blanco(self):
        peon = Pawn('WHITE')
        # Movimientos desde la posición inicial (6, 3)
        movimientos_esperados_inicial = [(5, 3), (4, 3)]
        self.assertEqual(peon.possible_moves(6, 3), movimientos_esperados_inicial)
        
        # Movimientos desde una posición intermedia (5, 3)
        movimientos_esperados_intermedios = [(4, 3), (4, 2), (4, 4)]  # Incluye movimientos diagonales
        self.assertEqual(peon.possible_moves(5, 3), movimientos_esperados_intermedios)
        
        # Verifica los movimientos diagonales desde (5, 3)
        movimientos = peon.possible_moves(5, 3)
        self.assertIn((4, 2), movimientos)
        self.assertIn((4, 4), movimientos)

# Evalúa los posibles movimientos del peón negro desde varias posiciones. Llama al método possible_moves con diferentes posiciones iniciales y compara los movimientos obtenidos.
    def test_movimientos_peon_negro(self):
        peon = Pawn('BLACK')
        # Movimientos desde la posición inicial (1, 3)
        movimientos_esperados_inicial = [(2, 3), (3, 3)]
        self.assertEqual(peon.possible_moves(1, 3), movimientos_esperados_inicial)
        
        # Movimientos desde una posición intermedia (2, 3)
        movimientos_esperados_intermedios = [(3, 3), (3, 2), (3, 4)]  # Incluye movimientos diagonales
        self.assertEqual(peon.possible_moves(2, 3), movimientos_esperados_intermedios)
        
        # Verifica los movimientos diagonales desde (2, 3)
        movimientos = peon.possible_moves(2, 3)
        self.assertIn((3, 2), movimientos)
        self.assertIn((3, 4), movimientos)

if __name__ == '__main__':
    unittest.main()
