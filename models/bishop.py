from models.piece import Piece
from util.move import *


class Bishop(Piece):
    def __init__(self, row, col, color, img, house):
        super(Bishop, self).__init__(row, col, color, img, house)

    def get_type(self):
        return self.__str__()

    def __str__(self):
        return "Bishop"

    def update_possible_moves(self, board):
        pos = self.house.get_position()
        self.move_list = all_down_left_moves(pos, board, self.color) + \
                         all_down_right_moves(pos, board, self.color) + \
                         all_up_left_moves(pos, board, self.color) + \
                         all_up_right_moves(pos, board, self.color)
