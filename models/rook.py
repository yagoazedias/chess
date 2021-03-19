from models.piece import Piece
from util.move import *


class Rook(Piece):
    def __init__(self, row, col, color, img, house):
        super(Rook, self).__init__(row, col, color, img, house)
        self.is_first_move = True

    def get_type(self):
        return self.__str__()

    def __str__(self):
        return "Rook"

    def get_is_first_move(self):
        return self.is_first_move

    def set_is_first_move(self, value):
        self.is_first_move = value

    def update_possible_moves(self, board):
        pos = self.house.get_position()
        self.move_list = all_down_moves(pos, board, self.color) + \
                         all_up_moves(pos, board, self.color) + \
                         all_right_moves(pos, board, self.color) + \
                         all_left_moves(pos, board, self.color)
