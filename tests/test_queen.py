import unittest
from game.queen import Queen

class VerificarReina(unittest.TestCase):

    # Test para verificar que las direcciones de movimiento se inicializan correctamente en el constructor
    def test_direcciones_reina(self):
        reina = Queen('WHITE')
        direcciones_esperadas = [
            (-1, 0), (1, 0), (0, -1), (0, 1),  # Torre
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Alfil
        ]
        self.assertEqual(reina.__queen_king_directions__, direcciones_esperadas)

    # Test explícito del constructor (__init__)
    def test_queen_init(self):
        reina = Queen('WHITE')
        self.assertIsInstance(reina, Queen)

    # Test explícito del constructor para verificar el color
    def test_queen_init_color(self):
        reina_blanca = Queen('WHITE')
        reina_negra = Queen('BLACK')
        self.assertEqual(reina_blanca.__color__, 'WHITE')
        self.assertEqual(reina_negra.__color__, 'BLACK')

    # Test para verificar la representación en string (__str__)
    def test_representacion_str(self):
        reina_blanca = Queen('WHITE')
        reina_negra = Queen('BLACK')
        self.assertEqual(str(reina_blanca), '♕')
        self.assertEqual(str(reina_negra), '♛')

    # Test explícito del método __str__
    def test_queen_str_direct(self):
        reina = Queen('WHITE')
        self.assertEqual(reina.__str__(), '♕')
        reina_negra = Queen('BLACK')
        self.assertEqual(reina_negra.__str__(), '♛')

    # Test para verificar que se puede invocar possible_moves
    def test_invocar_possible_moves(self):
        reina = Queen('WHITE')
        self.assertTrue(hasattr(reina, 'possible_moves'))

    # Test explícito del método possible_moves
    def test_queen_possible_moves_call(self):
        reina = Queen('WHITE')
        movimientos = reina.possible_moves(3, 3)
        self.assertIsNotNone(movimientos)  # Solo verifica que el método se llama y no es None

    # Test de possible_moves con varias posiciones
    def test_queen_possible_moves_varios(self):
        reina = Queen('WHITE')
        self.assertIsNotNone(reina.possible_moves(0, 0))  # Esquina del tablero
        self.assertIsNotNone(reina.possible_moves(7, 7))  # Otra esquina del tablero
        self.assertIsNotNone(reina.possible_moves(3, 3))  # Centro del tablero

    # Test para verificar los movimientos disponibles de una reina blanca
    def test_movimientos_disponibles_blanco(self):
        reina = Queen('WHITE')
        fila_inicial, col_inicial = 3, 3
        movimientos_esperados = [
            # Movimientos como torre
            (2, 3), (1, 3), (0, 3),  # Arriba
            (4, 3), (5, 3), (6, 3), (7, 3),  # Abajo
            (3, 2), (3, 1), (3, 0),  # Izquierda
            (3, 4), (3, 5), (3, 6), (3, 7),  # Derecha
            # Movimientos como alfil
            (2, 2), (1, 1), (0, 0),  # Diagonal superior izquierda
            (2, 4), (1, 5), (0, 6),  # Diagonal superior derecha
            (4, 2), (5, 1), (6, 0),  # Diagonal inferior izquierda
            (4, 4), (5, 5), (6, 6), (7, 7)  # Diagonal inferior derecha
        ]
        movimientos_resultantes = reina.possible_moves(fila_inicial, col_inicial)
        self.assertEqual(sorted(movimientos_resultantes), sorted(movimientos_esperados))

    # Test para verificar los movimientos disponibles de una reina negra
    def test_movimientos_disponibles_negro(self):
        reina = Queen('BLACK')
        fila_inicial, col_inicial = 3, 3
        movimientos_esperados = [
            # Movimientos como torre
            (2, 3), (1, 3), (0, 3),  # Arriba
            (4, 3), (5, 3), (6, 3), (7, 3),  # Abajo
            (3, 2), (3, 1), (3, 0),  # Izquierda
            (3, 4), (3, 5), (3, 6), (3, 7),  # Derecha
            # Movimientos como alfil
            (2, 2), (1, 1), (0, 0),  # Diagonal superior izquierda
            (2, 4), (1, 5), (0, 6),  # Diagonal superior derecha
            (4, 2), (5, 1), (6, 0),  # Diagonal inferior izquierda
            (4, 4), (5, 5), (6, 6), (7, 7)  # Diagonal inferior derecha
        ]
        movimientos_resultantes = reina.possible_moves(fila_inicial, col_inicial)
        self.assertEqual(sorted(movimientos_resultantes), sorted(movimientos_esperados))

if __name__ == '__main__':
    unittest.main()
