from models.house import House
from constants.colors import *


class Board:

    def __init__(self):
        self.turn = 0
        self.winner = None
        self.houses = self.build_houses()

    def draw(self, display):
        for row in range(0, 8):
            for col in range(0, 8):
                self.houses[row][col].draw(display)

    def build_houses(self):
        houses = [[0 for _ in range(8)] for __ in range(8)]
        for row in range(0, 8):
            color_index = row % 2
            for col in range(0, 8):
                color = WHITE if color_index == 0 else BLACK
                houses[row][col] = House(row, col, color)
                color_index = (color_index + 1) % 2
        return houses

    def get_danger_moves(self):
        print("get_danger_moves")

    def is_checked(self):
        print("is_checked")
        return False

    def move_piece(self):
        print("move_piece")

    def get_house(self, pos):
        row = pos[0]
        col = pos[1]
        return self.houses[row][col]

    # verifica se a posicao pos tem um oponente
    def has_oponent(self, pos, my_color):
        row = pos[0]
        col = pos[1]
        return my_color != self.houses[row][col].get_piece().get_color() and not (self.houses[row][col].is_empty())

    # verifica se a posicao pos é valida. ou seja, esta dentro dos limites do tabuleiro
    def is_valid_pos(self, pos):
        row = pos[0]
        col = pos[1]
        return 0 <= row <= 7 and 0 <= col <= 7

    def get_piece(self, pos):
        return self.get_house(pos).get_piece()

    def is_empty(self, pos):
        return self.get_house(pos).is_empty()

    # verifica se a posicao pos tem um companheiro de equipe
    def has_teammate(self, pos, my_color):
        return my_color == self.get_house(pos).get_piece().get_color()
