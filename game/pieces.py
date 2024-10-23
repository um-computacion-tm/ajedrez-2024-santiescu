king_queen_mov = [(-1,0),(1,0),(0,-1),(0,1)]+[(-1,-1),(-1,1),(1,-1),(1,1)]

class Piece:
    
    def __init__(self, color):
        self.__color__ = color
        self.__dir_king_queen__ = king_queen_mov

    def possible_moves_gen(self, fila_inicio, columna_inicio, direcciones, one_step=False):
        movimientos = []
        for direccion in direcciones:
            nueva_fila, nueva_columna = fila_inicio, columna_inicio
            while True:
                nueva_fila += direccion[0]
                nueva_columna += direccion[1]
                if 0 <= nueva_fila < 8 and 0 <= nueva_columna < 8:
                    movimientos.append((nueva_fila, nueva_columna))
                    if one_step:
                        break
                else:
                    break
        return movimientos
        
    def get_color(self):
        return self.__color__

    def tried(self):
        return True