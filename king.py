from pieces import Piece

class King(Piece):
    white_str = ""
    black_str = ""

    def get_possible_positions(self, from_row, from_col):
        possibles = self.possible_orthogonal_positions(
            from_row,
            from_col,
        ) + self.possible_diagonal_positions(
            from_row,
            from_col,
        )
        possible_king = []
        for (possible_row, possible_col) in possibles:
            if (
                abs(from_row - possible_row) <= 1 and
                abs(from_col - possible_col) <= 1
            ):
                possible_king.append((possible_row, possible_col))
        return possible_king
