import pygame
from constants.colors import *


class Piece(object):
    def __init__(self, color, img, house):
        self.color = color
        self.img = img
        self.move_list = []
        self.house = house

    def draw(self, windows, x, y):
        draw_this = pygame.transform.scale(self.img, (27, 27))
        windows.blit(draw_this, (x + 10, y + 10))

    def get_color(self):
        return self.color

    def get_possible_moves(self, match):
        self.move_list = []
        self.update_possible_moves(match)
        return self.move_list

    def update_possible_moves(self, match):
        pass

    def get_house(self):
        return self.house
