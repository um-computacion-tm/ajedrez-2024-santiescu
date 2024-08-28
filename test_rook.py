import unittest
from pieces import Rook
from board import Board
class TestRook(unittest.TestCase):
       
    def test_str(self):
        board=Board()
        rook=Rook('WHITE',board)
        self.assertEqual(str(rook),'W')
            
    def test_move_vertical_desc(self):
        board=Board()
        rook=Rook('WHITE',board)
        possibles=rook.possible_positions(4,1)
        self.assertEqual(possibles,[(5,1),(6,1),(7,1)])