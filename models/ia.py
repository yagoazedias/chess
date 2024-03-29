from constants.colors import *
from random import choices
from models.minimax_ia import MinimaxIA

class Ia:
    def __init__(self, match):
        self.match = match
        self.minimax_ia = MinimaxIA()


    def move(self):
            
        #para voltar a IA com movimentos aleatórios, é só comentar
        #essas duas linhas abaixo, e descomentar essa terceira que está comentada.
        positions = self.minimax_ia.play(self.match)
        #positions = self.select_piece_and_desired_house()

        selected_house = positions[0]
        desired_house = positions[1]

        self.match.movement_manager(selected_house, desired_house)

    def select_piece_and_desired_house(self):
        position = (-1, -1)
        possible_moves = []
        selected_piece = None
        while True:
            position = choices(self.search_blacks())[0]
            selected_piece = self.match.board.get_house(position)

            possible_moves = selected_piece.get_piece().get_possible_moves(self.match)
            if len(possible_moves) > 0:
                break

        move = choices(possible_moves)[0]
        desired_house = self.match.board.get_house(move)
        return selected_piece, desired_house

    def search_blacks(self):
        positions = []
        for col in range(0, 8):
            for row in range(0, 8):
                if self.match.board.houses[col][row].get_piece() is not None:
                    if self.match.board.houses[col][row].get_piece().get_color() == BLACK:
                        positions.append((col, row))
        return positions
