from models.piece import Piece
from util.move import *


class Rook(Piece):
    def __init__(self, col, row, color, img, house):
        super(Rook, self).__init__(col, row, color, img, house)
        self.is_first_move = True

    def get_type(self):
        return self.__str__()

    def __str__(self):
        return "Rook"
    
    def set_is_first_move(self, condition):
        self.is_first_move = condition

    def get_is_first_move(self):
        return self.is_first_move

    def update_possible_moves(self, match):
        pos = self.house.get_position()
        self.move_list = all_down_moves(pos, match, self.color) + \
                         all_up_moves(pos, match, self.color) + \
                         all_right_moves(pos, match, self.color) + \
                         all_left_moves(pos, match, self.color)
