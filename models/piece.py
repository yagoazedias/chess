import pygame


class Piece(object):
    def __init__(self, col, row, color, img, house):
        self.col = col
        self.row = row
        self.color = color
        self.img = img
        self.selected = False
        self.move_list = []
        self.house = house

    def is_selected(self):
        return self.selected

    def set_selected(self, value):
        self.selected = value

    def draw(self, windows, x, y):
        draw_this = (
            pygame.transform.scale(self.img, (27, 27))
            if self.color == "white"
            else pygame.transform.scale(self.img, (27, 27))
        )

        if self.selected:
            pygame.draw.rect(windows, 0, (x + 10, y + 10, 31, 31), 2)

        windows.blit(draw_this, (x + 10, y + 10))

    def update_position(self, col, row):
        self.col = col
        self.row = row

    def get_color(self):
        return self.color

    def get_position(self):
        return self.col, self.row

    def get_possible_moves(self, board):
        self.move_list = []
        self.update_possible_moves(board)
        return self.move_list

    def update_possible_moves(self, board):
        pass
