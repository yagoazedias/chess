import pygame
from constants.colors import *


class House:
    def __init__(self, column, row, color):
        self.column = column
        self.row = row
        self.position_column = column * 50
        self.position_row = row * 50
        self.is_high_light = False
        self.house_color = color
        self.color = color
        self.piece = None

    def get_position_column(self):
        return self.position_column

    def get_position_row(self):
        return self.position_row

    def get_position(self):
        return int(self.get_position_column() / 50), int(self.get_position_row() / 50)

    def set_piece(self, piece):
        if piece:
            piece.house = self
        self.piece = piece

    def draw(self, display):
        pygame.draw.rect(
            display, self.color, (self.position_column, self.position_row, 50, 50)
        )
        if self.piece is not None:
            self.piece.draw(display, self.position_column, self.position_row)

    def get_piece(self):
        return self.piece

    def is_empty(self):
        return self.piece is None

    def set_color(self):
        if self.house_color == WHITE:
            self.color = (
                self.house_color if not self.is_high_light else WHITE_HIGH_LIGHT
            )
        else:
            self.color = (
                self.house_color if not self.is_high_light else BLACK_HIGH_LIGHT
            )

    def set_is_high_light(self, condition):
        self.is_high_light = condition
        self.set_color()

    def get_is_high_light(self):
        return self.is_high_light
