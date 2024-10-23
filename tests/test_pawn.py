import unittest
from game.pawn import Pawn
from game.board import Board


class TestPawn(unittest.TestCase):

    def test_initial_black(self):
        board = Board(for_test = True)
        pawn = Pawn("BLACK", board)

        possibles = pawn.get_possible_positions(1, 5)
        self.assertEqual(
            possibles,
            [(2, 5), (3, 5)]
        )

    def test_tried (self): 
        board = Board(for_test = True)
        pawn = Pawn("BLACK", board)
        self.assertTrue(pawn.tried())
