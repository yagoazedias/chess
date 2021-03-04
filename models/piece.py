import pygame


class Piece(object):

    def __init__(self, row, col, color, img):
        self.row = row
        self.col = col
        self.color = color
        self.img = img
        self.selected = False
        self.move_list = []

    def is_selected(self):
        return self.selected

    def draw(self, windows, x, y):
        draw_this = pygame.transform.scale(self.img, (55, 55)) if self.color == "white" \
            else pygame.transform.scale(self.img, (55, 55))

        if self.selected:
            pygame.draw.rect(windows, 0, (x + 20, y + 20, 62, 62), 2)

        windows.blit(draw_this, (x + 20, y + 20))

    def update_position(self, r, c):
        self.row = r
        self.col = c

    def get_color(self):
        return self.color

    def get_position(self):
        return self.row, self.col

    def get_possible_moves(self):
        return self.move_list

    def update_possible_moves(self, board):
        pass
