from pieces import Piece

class Bishop(Piece):
    white_str = ""
    black_str = ""

    def get_possible_positions(self, from_row, from_col):
        return self.possible_diagonal_positions(
            from_row,
            from_col,
        )