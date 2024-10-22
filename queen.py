from pieces import Piece

class Queen(Piece):
    white_str = "♛"
    black_str = "♕"

    def get_possible_positions(self, from_row, from_col):
        return self.possible_orthogonal_positions(
            from_row,
            from_col,
        ) + self.possible_diagonal_positions(
            from_row,
            from_col,
        )