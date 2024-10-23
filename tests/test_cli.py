import unittest
from io import StringIO
from game.chess import Chess
from game.cli import play as play, render_board_with_icons as show_board_with_icons
from unittest.mock import patch, MagicMock, Mock
from game.exceptions import InvalidPieceMoveError

class TestCli(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_board_with_icons(self, mock_stdout):
        board = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        ]
        show_board_with_icons(board)
        expected_output = (
            '♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜\n'
            '♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟\n'
            '· · · · · · · ·\n'
            '· · · · · · · ·\n'
            '· · · · · · · ·\n'
            '· · · · · · · ·\n'
            '♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙\n'
            '♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖\n'
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['EXIT'])
    def test_exit_game(self, mock_input, mock_stdout):
        chess = MagicMock()
        with self.assertRaises(SystemExit):
            play(chess)
        self.assertIn("Juego terminado.", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', 'EXIT'])
    def test_exit_mid_game(self, mock_input, mock_stdout):
        chess = MagicMock()
        with self.assertRaises(SystemExit):
            play(chess)
        self.assertIn("Juego terminado.", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', '1', 'EXIT'])
    def test_exit_later(self, mock_input, mock_stdout):
        chess = MagicMock()
        with self.assertRaises(SystemExit):
            play(chess)
        self.assertIn("Juego terminado.", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['6', '0', '4', '0'])
    @patch('chess.cli.render_board_with_icons')
    def test_valid_move_pawn(self, mock_render_board, mock_input, mock_stdout):
        chess = MagicMock()
        chess.get_board.return_value = [['.'] * 8 for _ in range(8)]
        chess.turno = 'WHITE'
        play(chess)
        chess.move.assert_called_with(6, 0, 4, 0)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['7', '1', '5', '0'])
    @patch('chess.cli.render_board_with_icons')
    def test_valid_move_knight1(self, mock_render_board, mock_input, mock_stdout):
        chess = MagicMock()
        chess.get_board.return_value = [['.'] * 8 for _ in range(8)]
        chess.turno = 'WHITE'
        play(chess)
        chess.realizar_movimiento.assert_called_with(7, 1, 5, 0)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['7', '1', '5', '0'])
    def test_valid_move_knight_black(self, mock_stdout, mock_input):
        chess = MagicMock()
        chess.get_board.return_value = [['.'] * 8 for _ in range(8)]
        chess.turno = 'BLACK'
        play(chess)
        chess.realizar_movimiento.assert_called_with(7, 1, 5, 0)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['0', '0', '8', '1', '0', '0', 'EXIT'])
    def test_invalid_coordinates(self, mock_input, mock_stdout):
        chess = MagicMock()
        chess.get_board.return_value = [['.'] * 8 for _ in range(8)]
        chess.turno = 'WHITE'
        play(chess)
        self.assertIn("Entrada inválida. Por favor ingresa un número entre 0 y 7.", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['0', '0', '1', '1', 'EXIT'])
    def test_symbol_coordinates(self, mock_input, mock_stdout):
        chess = Mock(spec=['get_board', 'turno', 'realizar_movimiento'])
        chess.get_board.return_value = [['.'] * 8 for _ in range(8)]
        chess.turno = 'WHITE'
        chess.realizar_movimiento.side_effect = InvalidPieceMoveError("Invalid move for the selected piece.")

        play(chess)
        self.assertIn("Turno actual: WHITE", mock_stdout.getvalue())
        self.assertIn("Movimiento inválido: Invalid move for the selected piece.", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['a', 'b', 'c', 'd', '0', '0', '0', '0', 'EXIT'])
    def test_non_numeric_input(self, mock_input, mock_stdout):
        chess = MagicMock()
        chess.get_board.return_value = [['.'] * 8 for _ in range(8)]
        chess.turno = 'WHITE'
        play(chess)
        self.assertIn("Entrada inválida. Por favor ingresa un número entre 0 y 7.", mock_stdout.getvalue())
    
    @patch('builtins.exit', side_effect=SystemExit)  # Simulamos `exit()` lanzando `SystemExit`
    @patch('builtins.input', side_effect=['7', '1', '5', '0', 'EXIT'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_valid_move_then_exit(self, mock_stdout, mock_input, mock_exit):
        chess = MagicMock(spec=Chess)
        chess.get_board.return_value = [['.'] * 8 for _ in range(8)]
        chess.turno = 'WHITE'
        chess.realizar_movimiento.return_value = None  # Simulamos un movimiento exitoso
        play(chess)

        # Verificamos que se realizó el movimiento correcto
        chess.realizar_movimiento.assert_called_with(7, 1, 5, 0)
        with self.assertRaises(SystemExit):
            play(chess)  # Ejecutamos el juego

        # Verificamos que se haya llamado a `exit()`
        mock_exit.assert_called_once()

        # Comprobamos la salida esperada
        self.assertIn("Juego terminado.", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()