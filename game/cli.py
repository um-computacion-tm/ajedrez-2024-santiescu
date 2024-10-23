from chess import Chess
from exceptions import InvalidMove, InvalidTurn, EmptyPosition

def main ():
    chess = Chess()
    while True:
        play(chess)

def play(chess):
    try:
        print(chess.show_board())
        print("turn: ", chess.turn)
        from_row= int(input("From row: "))
        from_col= int(input("From col: "))
        to_row= int(input("To row: "))
        to_col= int(input("To col: "))
    
        chess.move(
            from_row,
            from_col,
            to_row,
            to_col
        )
    
    except InvalidMove as e:
        print(e)
    except Exception as e:
        print("error", e)


if __name__ == '__main__':
    main()
    