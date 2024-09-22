import unittest
from board import Board
from pieces import Rook, Pawn

class TestBoard(unittest.TestCase):
    def test_str_board(self):
        board = Board()
        board.set_piece(0, 0, Rook("WHITE", board))
        board.set_piece(0, 1, Rook("WHITE", board))
        board.set_piece(1, 0, Pawn("WHITE", board))
        board.set_piece(1, 1, Pawn("WHITE", board))
        expected_str = (
            "♖ ♖ . . . . . .\n"
            "♙ ♙ . . . . . .\n"
            ". . . . . . . .\n"
            ". . . . . . . .\n"
            ". . . . . . . .\n"
            ". . . . . . . .\n"
            ". . . . . . . .\n"
            "♜ ♜ ♜ ♜ ♜ ♜ ♜ ♜"
        )
        self.assertEqual(str(board), expected_str)

    def test_get_piece_out_of_range_row_and_col(self):
        board = Board()
        with self.assertRaises(IndexError):
            board.get_piece(10, 10)

    def test_set_piece_out_of_range_row_and_col(self):
        board = Board()
        rook = Rook("WHITE", board)
        with self.assertRaises(IndexError):
            board.set_piece(10, 10, rook)

    def test_move(self):
        board = Board()
        rook = Rook("WHITE", board)
        board.set_piece(0, 0, rook)
        board.move(0, 0, 4, 4)  # Cambié de move_piece a move
        expected_str = (
            ". . . . . . . .\n"
            ". . . . . . . .\n"
            ". . . . . . . .\n"
            ". . . . . . . .\n"
            ". . . . ♖ . . .\n"
            ". . . . . . . .\n"
            ". . . . . . . .\n"
            ". . . . . . . ."
        )
        self.assertEqual(str(board), expected_str)

    def test_set_piece_in_range(self):
        board = Board()
        rook = Rook("WHITE", board)
        board.set_piece(0, 0, rook)
        self.assertIsInstance(board.get_piece(0, 0), Rook)
        board.set_piece(0, 0, None)
        self.assertIsNone(board.get_piece(0, 0))

if __name__ == '__main__':
    unittest.main()