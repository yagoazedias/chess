import pygame


class House:

    def __init__(self, row, column, color):
        self.column = column
        self.row = row
        self.position_column = (column * 100)
        self.position_row = (row * 100)
        self.color = color

    def set_color(self, color):
        self.color = color

    def get_position_column(self):
        return self.position_column

    def get_position_row(self):
        return self.position_row

    def draw(self, display):
        pygame.draw.rect(display, self.color, (self.get_position_row(), self.get_position_column(), 100, 100))
