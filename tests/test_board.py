import unittest
from board import Board
from pieces import Pawn
from rook import Rook
from exceptions import OutOfBoard, RowOutOfBoard, ColumnOutOfBoard

class TestBoard(unittest.TestCase):

    # STR

    def test_str_board(self):
        board = Board()
        self.assertEqual(
            str(board),
            (
                "♖      ♖\n"
                "♙♙♙♙♙♙♙♙\n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "♟♟♟♟♟♟♟♟\n"
                "♜      ♜\n"
            )
        )
    
    # GET_PIECE METHOD

    def test_get_piece_in_range(self):
        board=Board()
        self.assertIsInstance(board.get_piece(0,0),Rook)
        self.assertIsNone(board.get_piece(2,0))

    def test_get_piece_out_of_range_row_and_col(self):
        board = Board(for_test=True)
        with self.assertRaises(OutOfBoard) as exc:
            board.get_piece(10, 10)
        self.assertEqual(
            exc.exception.message,
            "La posicion indicada se encuentra fuera del tablero"
        )

    def test_get_piece_out_of_range_row(self):
        board = Board(for_test=True)
        with self.assertRaises(RowOutOfBoard) as exc:
            board.get_piece(10, 0)
        self.assertEqual(
            exc.exception.message,
            "La Fila indicada se encuentra fuera del tablero"
        )

    def test_get_piece_out_of_range_col(self):
        board = Board(for_test=True)
        with self.assertRaises(ColumnOutOfBoard) as exc:
            board.get_piece(0, 10)
        self.assertEqual(
            exc.exception.message,
            "La Columna indicada se encuentra fuera del tablero"
        )

    # SET_PIECE METHOD

    def test_set_piece_in_range(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        self.assertIsNone(board.get_piece(0,0))
        board.set_piece(0,0,rook)
        self.assertIsInstance(board.get_piece(0,0),Rook)

    def test_set_piece_out_of_range_row_and_col(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        with self.assertRaises(OutOfBoard) as exc:
            board.set_piece(10, 10,rook)
        self.assertEqual(
            exc.exception.message,
            "La posicion indicada se encuentra fuera del tablero"
        )

    def test_set_piece_out_of_range_row(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        with self.assertRaises(RowOutOfBoard) as exc:
            board.set_piece(10, 0,rook)
        self.assertEqual(
            exc.exception.message,
            "La Fila indicada se encuentra fuera del tablero"
        )
    
    def test_set_piece_out_of_range_col(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        with self.assertRaises(ColumnOutOfBoard) as exc:
            board.set_piece(0, 10,rook)
        self.assertEqual(
            exc.exception.message,
            "La Columna indicada se encuentra fuera del tablero"
        )

    # PUTTING ROOKS ON THE BOARD WHEN STARTING THE GAME

    def test_rooks_creation(self):
        board=Board()
        self.assertIsInstance(board.get_piece(0,0),Rook)
        self.assertEqual(board.get_piece(0,0).__color__,'BLACK')
        self.assertIsInstance(board.get_piece(0,7),Rook)
        self.assertEqual(board.get_piece(0,7).__color__,'BLACK')
        self.assertIsInstance(board.get_piece(7,0),Rook)
        self.assertEqual(board.get_piece(7,0).__color__,'WHITE')
        self.assertIsInstance(board.get_piece(7,7),Rook)
        self.assertEqual(board.get_piece(7,7).__color__,'WHITE')

    # PUTTING PAWNS ON THE BOARD WHEN STARTIGN THE GAME

    def test_pawns_creation(self):
        board=Board()
        self.assertIsInstance(board.get_piece(1,0),Pawn)
        self.assertEqual(board.get_piece(1,0).__color__,'BLACK')
        self.assertIsInstance(board.get_piece(1,1),Pawn)
        self.assertEqual(board.get_piece(1,1).__color__,'BLACK')
        self.assertIsInstance(board.get_piece(1,2),Pawn)
        self.assertEqual(board.get_piece(1,2).__color__,'BLACK')
        self.assertIsInstance(board.get_piece(1,3),Pawn)
        self.assertEqual(board.get_piece(1,3).__color__,'BLACK')
        self.assertIsInstance(board.get_piece(1,4),Pawn)
        self.assertEqual(board.get_piece(1,4).__color__,'BLACK')
        self.assertIsInstance(board.get_piece(1,5),Pawn)
        self.assertEqual(board.get_piece(1,5).__color__,'BLACK')
        self.assertIsInstance(board.get_piece(1,6),Pawn)
        self.assertEqual(board.get_piece(1,6).__color__,'BLACK')
        self.assertIsInstance(board.get_piece(1,7),Pawn)
        self.assertEqual(board.get_piece(1,7).__color__,'BLACK')
        self.assertIsInstance(board.get_piece(6,0),Pawn)
        self.assertEqual(board.get_piece(6,0).__color__,'WHITE')
        self.assertIsInstance(board.get_piece(6,1),Pawn)
        self.assertEqual(board.get_piece(6,1).__color__,'WHITE')
        self.assertIsInstance(board.get_piece(6,2),Pawn)
        self.assertEqual(board.get_piece(6,2).__color__,'WHITE')
        self.assertIsInstance(board.get_piece(6,3),Pawn)
        self.assertEqual(board.get_piece(6,3).__color__,'WHITE')
        self.assertIsInstance(board.get_piece(6,4),Pawn)
        self.assertEqual(board.get_piece(6,4).__color__,'WHITE')
        self.assertIsInstance(board.get_piece(6,5),Pawn)
        self.assertEqual(board.get_piece(6,5).__color__,'WHITE')
        self.assertIsInstance(board.get_piece(6,6),Pawn)
        self.assertEqual(board.get_piece(6,6).__color__,'WHITE')
        self.assertIsInstance(board.get_piece(6,7),Pawn)
        self.assertEqual(board.get_piece(6,7).__color__,'WHITE')

    # EMPTY SPACES ON THE BOARD WHEN STARTING THE GAME

    def test_empty_spaces(self):
        board=Board()
        self.assertIsNone(board.get_piece(2,0))
        self.assertIsNone(board.get_piece(2,1))
        self.assertIsNone(board.get_piece(2,2))
        self.assertIsNone(board.get_piece(2,3))
        self.assertIsNone(board.get_piece(2,4))
        self.assertIsNone(board.get_piece(2,5))
        self.assertIsNone(board.get_piece(2,6))
        self.assertIsNone(board.get_piece(2,7))
        self.assertIsNone(board.get_piece(3,0))
        self.assertIsNone(board.get_piece(3,1))
        self.assertIsNone(board.get_piece(3,2))
        self.assertIsNone(board.get_piece(3,3))
        self.assertIsNone(board.get_piece(3,4))
        self.assertIsNone(board.get_piece(3,5))
        self.assertIsNone(board.get_piece(3,6))
        self.assertIsNone(board.get_piece(3,7))
        self.assertIsNone(board.get_piece(4,0))
        self.assertIsNone(board.get_piece(4,1))
        self.assertIsNone(board.get_piece(4,2))
        self.assertIsNone(board.get_piece(4,3))
        self.assertIsNone(board.get_piece(4,4))
        self.assertIsNone(board.get_piece(4,5))
        self.assertIsNone(board.get_piece(4,6))
        self.assertIsNone(board.get_piece(4,7))
        self.assertIsNone(board.get_piece(5,0))
        self.assertIsNone(board.get_piece(5,1))
        self.assertIsNone(board.get_piece(5,2))
        self.assertIsNone(board.get_piece(5,3))
        self.assertIsNone(board.get_piece(5,4))
        self.assertIsNone(board.get_piece(5,5))
        self.assertIsNone(board.get_piece(5,6))
        self.assertIsNone(board.get_piece(5,7))

    # MOVE METHOD

    def test_move(self):
        board=Board(for_test=True)
        rook=Rook(color='BLACK', board=board)
        board.set_piece(0, 0, rook)
        board.move(0,0,0,1)

        self.assertIsInstance(
            board.get_piece(0, 1),
            Rook)
        
        self.assertEqual(
            str(board),
            (
                " ♖      \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
            )
        )

    

if __name__=='__main__':
    unittest.main()