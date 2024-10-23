from game.chess import Chess
from game.exceptions import InvalidMove, GameOverException, NonPieceOriginError, WrongTurnError, InvalidPieceMoveError

def main ():
    chess = Chess()
    while True:
        try:
            play(chess)
        except GameOverException as game_end:
            print(str(game_end))
            print("Juego terminado.")
            break
def render_board_with_icons(tablero):   
    piezas_icons = {
        'R': '♜', 'N': '♞', 'B': '♝', 'Q': '♛', 'K': '♚', 'P': '♟',
        'r': '♖', 'n': '♘', 'b': '♗', 'q': '♕', 'k': '♔', 'p': '♙',
        '.': '·'  
    }
    for fila in tablero:
        print(' '.join(piezas_icons.get(pieza, '.') for pieza in fila))


def play(chess):
    try:
        render_board_with_icons(chess.get_board())
        print("Indica las coordenadas de la pieza que quieres mover y su destino.")
        print("Escribe EXIT para finalizar la partida.")
        print("Turno actual:", chess.turno)

        origen_fila = obtener_input("Fila de origen: ")
        origen_columna = obtener_input("Columna de origen: ")
        destino_fila = obtener_input("Fila de destino: ")
        destino_columna = obtener_input("Columna de destino: ")

        origen_fila, origen_columna, destino_fila, destino_columna = map(int, [origen_fila, origen_columna, destino_fila, destino_columna])

        chess.move(origen_fila, origen_columna, destino_fila, destino_columna)

        print("DEBUG: Movement completed, checking for next input.")
        
    except (InvalidMove, NonPieceOriginError, WrongTurnError, InvalidPieceMoveError) as error:
        print("Movimiento inválido:", error)

def obtener_input(prompt):
    while True:
        valor = input(prompt)
        if valor.upper() == "EXIT":
            print("Juego terminado.")
            exit()  
        if valor.isdigit() and 0 <= int(valor) < 8:
            return valor
        print("Entrada inválida. Por favor ingresa un número entre 0 y 7.")


if __name__ == '__main__':
    main()
    