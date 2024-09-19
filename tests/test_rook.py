import unittest
from pieces import Pawn
from board import Board
from rook import Rook

class TestRook(unittest.TestCase):
    def test_str(self):
        board = Board()
        rook = Rook('WHITE', board)  
        self.assertEqual(str(rook), '♜')

    def test_move_vertical_desc(self):
        board = Board()
        board.__positions__[5][1] = None
        board.__positions__[6][1] = None
        board.__positions__[7][1] = None
        rook = Rook('WHITE', board)  
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(possibles, [(5, 1), (6, 1), (7, 1)])

    def test_move_vertical_asc(self):
        board = Board()
        rook = Rook('WHITE', board)  
        possibles = rook.possible_positions_va(4, 1)
        self.assertEqual(possibles, [(3, 1), (2, 1), (1, 1), (0, 1)])
    
    def test_move_vertical_desc_with_own_pieces(self):
        board = Board()
        board.__positions__[5][1] = None
        board.__positions__[6][1] = Pawn("BLACK", board)
        rook = Rook("BLACK", board)  
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(possibles, [(5, 1)])

    def test_move_vertical_desc_with_not_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("BLACK", board))
        rook = Rook("WHITE", board)  
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(possibles, [(5, 1), (6, 1)])

    def test_move_horizontal_right(self):
        board = Board()
        rook = Rook('WHITE', board)  
        possibles = rook.possible_positions_hr(4, 1)
        self.assertEqual(possibles, [(4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7)])

    def test_move_horizontal_left(self):
        board = Board()
        rook = Rook('WHITE', board)  
        possibles = rook.possible_positions_hl(4, 1)
        self.assertEqual(possibles, [(4, 0)])

    def test_valid_positions(self):
        board = Board()
        rook = Rook('WHITE', board)
        board.set_piece(4, 1, rook)
        valid_positions = rook.valid_positions(4, 1, 4, 2)  # Moving right
        self.assertTrue(valid_positions)
        valid_positions = rook.valid_positions(4, 1, 3, 1)  # Moving up
        self.assertTrue(valid_positions)
        valid_positions = rook.valid_positions(4, 1, 5, 1)  # Moving down
        self.assertTrue(valid_positions)
        valid_positions = rook.valid_positions(4, 1, 4, 0)  # Moving left
        self.assertTrue(valid_positions)

if __name__ == '__main__':
    unittest.main()
