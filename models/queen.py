from models.piece import Piece
from util.move import *


class Queen(Piece):
    def __init__(self, col, row, color, img, house):
        super(Queen, self).__init__(col, row, color, img, house)

    def get_type(self):
        return self.__str__()

    def __str__(self):
        return "Queen"

    def update_possible_moves(self, board):
        pos = self.house.get_position()
        self.move_list = all_down_moves(pos, board, self.color) + \
                         all_up_moves(pos, board, self.color) + \
                         all_right_moves(pos, board, self.color) + \
                         all_left_moves(pos, board, self.color) + \
                         all_up_left_moves(pos, board, self.color) + \
                         all_down_left_moves(pos, board, self.color) + \
                         all_down_right_moves(pos, board, self.color) + \
                         all_up_right_moves(pos, board, self.color)
