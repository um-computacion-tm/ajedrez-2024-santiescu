import unittest
from chess import Chess


class TestChess(unittest.TestCase):
    def setUp(self):
        self.chess=Chess()
    def test_turno_inicial(self):
        self.assertEqual(self.chess.turn(),'WHITE')
    def test_change_turn_white_to_black(self):
        self.chess.change_turn()
        self.assertEqual(self.chess.turn(),'BLACK')

    if __name__ == '__main__':
        unittest.main()