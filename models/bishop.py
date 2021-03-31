from models.piece import Piece
from util.move import *
from constants.colors import *


class Bishop(Piece):
    def __init__(self, color, img, house):
        super(Bishop, self).__init__(color, img, house)


        
    def get_value(self):
        if self.get_color() == WHITE:
            return 30
        else:
            return -30
            
    def get_type(self):
        return self.__str__()

    def __str__(self):
        return "Bishop"

    def update_possible_moves(self, match):
        pos = self.house.get_position()
        self.move_list = all_down_left_moves(pos, match, self.color) + \
                         all_down_right_moves(pos, match, self.color) + \
                         all_up_left_moves(pos, match, self.color) + \
                         all_up_right_moves(pos, match, self.color)
