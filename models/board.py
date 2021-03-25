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

    def get_danger_moves(self):
        print("get_danger_moves")

    def is_checked(self):
        print("is_checked")
        return False

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

    def move(self, selected_piece, selected_piece_house, captured_piece, desired_house):
        # captured_piece = desired_house.get_piece()
        desired_house.set_piece(selected_piece)
        self.get_selected_piece_house().set_piece(None)
        return captured_piece

    def undo_move(self, selected_piece, desired_house, captured_piece, captured_piece_house, new_rook_house):
        if new_rook_house is not None:
            new_rook_house.set_piece(None)
        if desired_house.get_position != captured_piece_house:
            desired_house.set_piece(None)
        if captured_piece is not None:
            captured_piece_house.set_piece(captured_piece)
        self.get_selected_piece_house().set_piece(selected_piece)
