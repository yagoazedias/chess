from constants.colors import *
from models.house import House


class Board:

    def __init__(self):
        self.turn = 0
        self.winner = None
        self.houses = [[0 for _ in range(7)] for __ in range(7)]
        self.set_up()

    def draw(self, display):
        for row in range(0, 7):
            for col in range(0, 7):
                self.houses[row][col].draw(display)

    def set_up(self):
        for row in range(0, 7):
            color_index = row % 2
            for col in range(0, 7):
                color = WHITE if color_index == 0 else BLACK
                self.houses[row][col] = House(row, col, color)
                color_index = (color_index + 1) % 2

    def get_danger_moves(self):
        print("get_danger_moves")

    def is_checked(self):
        print("is_checked")
        return False

    def move_piece(self):
        print("move_piece")
