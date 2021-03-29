from constants.colors import *


class Board:
    def __init__(self, houses):
        self.selected_piece_house = None
        self.turn = WHITE
        self.winner = None
        self.houses = houses

    def set_selected_piece_house(self, house):
        if house is not None:
            house.set_selected(True)
        self.selected_piece_house = house

    def get_selected_piece_house(self):
        return self.selected_piece_house

    def clean_highlight(self):
        for col in range(0, 8):
            for row in range(0, 8):
                self.houses[col][row].set_is_highlight(False)
                self.houses[col][row].set_selected(False)

    # TODO: descobrir porque recebe uma tuple pos
    def get_house(self, pos):
        col = pos[0]
        row = pos[1]
        return self.houses[col][row]

    # verifica se a posicao pos tem um oponente
    def has_opponent(self, pos, piece_color):
        if self.get_house(pos).get_piece() is None:
            return False
        return piece_color != self.get_house(pos).get_piece().get_color()

    def get_piece(self, pos):
        return self.get_house(pos).get_piece()

    def is_empty(self, pos):
        return self.get_house(pos).is_empty()
