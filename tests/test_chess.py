import unittest
from chess import Chess
from game.exceptions import NonPieceOriginError, WrongTurnError, InvalidPieceMoveError

class TestAjedrez(unittest.TestCase):
    def test_inicializacion(self):
        partida = Chess()  
        self.assertEqual(partida.turn, "WHITE")
        tablero = partida.get_board()
        self.assertIsNotNone(tablero)

    def test_realizar_movimientor_peon_valido(self):
        partida = Chess()
        partida.move(6, 0, 4, 0)
        self.assertEqual(partida.turn, "BLACK")
        self.assertEqual(partida.get_board()[6][0], '.')
        self.assertIsNotNone(partida.get_board()[4][0])

    def test_realizar_movimientor_caballo_valido(self):
        partida = Chess()
        partida.move(7, 1, 5, 2)
        self.assertEqual(partida.turn, "BLACK")
        self.assertEqual(partida.get_board()[7][1], '.')
        self.assertIsNotNone(partida.get_board()[5][2])

    def test_realizar_movimientor_sin_pieza1(self):
        partida = Chess()  
        with self.assertRaises(NonPieceOriginError) as contexto:
            partida.move(3, 3, 4, 3)  
        self.assertEqual(str(contexto.exception), "No hay ninguna pieza en la posición de origen.")

    def test_realizar_movimientor_sin_pieza2(self):
        partida = Chess()  
        with self.assertRaises(NonPieceOriginError) as contexto:
            partida.move(3, 4, 4, 4)  
        self.assertEqual(str(contexto.exception), "No hay ninguna pieza en la posición de origen.")

    def test_turno_incorrecto(self):
        partida = Chess()
        partida.move(6, 0, 4, 0)
        with self.assertRaises(WrongTurnError) as contexto:
            partida.move(6, 1, 5, 2)
        self.assertEqual(str(contexto.exception), "No es el turno de la pieza seleccionada.")

    def test_movimiento_invalido(self):
        partida = Chess()
        with self.assertRaises(InvalidPieceMoveError) as contexto:
            partida.move(6, 0, 3, 0)
        self.assertEqual(str(contexto.exception), "Movimiento no válido para la pieza seleccionada.")

    def test_alternar_turno(self):
        partida = Chess()
        partida.move(6, 0, 4, 0)
        self.assertEqual(partida.turn, "BLACK")
        partida.move(1, 0, 3, 0)
        self.assertEqual(partida.turn, "WHITE")

if __name__ == '__main__':
    unittest.main()
